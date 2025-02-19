
import cv2
import numpy as np
import mediapipe as mp
import gc
import logging
import torch
from scipy.signal import butter, filtfilt, correlate, savgol_filter
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2
from scripts.rppg_preprocessing import RPPGProcessor
from scripts.ptt_bp_preprocessing import PTTBPProcessor
from scripts.config import CONFIG
from scripts.deepphys_model import DeepPhys  # DeepPhys model definition

logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")

class VideoProcessor:
    """Handles full-video processing for rPPG extraction and BP estimation"""

    def __init__(self):
        """Initialize the face and hand landmark models, and load DeepPhys onto GPU if available."""
        try:
            base_options = python.BaseOptions(model_asset_path=CONFIG["FACE_MODEL_PATH"])
            options = vision.FaceLandmarkerOptions(
                base_options=base_options,
                running_mode=vision.RunningMode.VIDEO,
                output_face_blendshapes=True,
                output_facial_transformation_matrixes=True,
                num_faces=1,
            )
            self.face_landmarker_model = vision.FaceLandmarker.create_from_options(options)

            base_hand_options = python.BaseOptions(model_asset_path=CONFIG["HAND_MODEL_PATH"])
            hand_options = vision.HandLandmarkerOptions(
                base_options=base_hand_options,
                running_mode=vision.RunningMode.VIDEO,
                num_hands=2
            )
            self.hand_landmarker_model = vision.HandLandmarker.create_from_options(hand_options)

            # Process one out of every 5 frames
            self.sampling_factor = 5

        except Exception as e:
            logging.error(f"Failed to initialize models: {e}")
            raise

        self.face_roi_buffer = []
        self.hand_roi_buffer = []
        self.rppg_sequence_buffer = []
        # Reset the last timestamp for the first video
        self.last_timestamp_ms = -1  

        # --- Initialize the DeepPhys model on GPU (if available) ---
        try:
            self.deepphys_model = DeepPhys(img_size=72)  # Adjust img_size if needed
            # Load model weights mapping to CUDA
            state = torch.load(CONFIG["DEEP_PHYS_MODEL_PATH"], map_location=torch.device('cuda'))
            # Remove any DataParallel "module." prefixes
            new_state = {key.replace("module.", ""): value for key, value in state.items()}
            self.deepphys_model.load_state_dict(new_state)
            # Move model to GPU
            self.deepphys_model.to(torch.device('cuda'))
            self.deepphys_model.eval()
        except Exception as e:
            logging.error(f"Failed to initialize DeepPhys model: {e}")
            raise

    def extract_roi(self, frame, video_fps, face_landmarks=None, hand_landmarks=None):
        """
        Extracts ROI from a frame using face or hand landmarks.
        ROI is resized to (320, 240) for consistency.
        """
        h, w, _ = frame.shape
        COMMON_SIZE = (320, 240)

        if face_landmarks is not None:
            try:
                landmarks = face_landmarks.landmark if hasattr(face_landmarks, "landmark") else face_landmarks
                key_regions = [
                    mp.solutions.face_mesh.FACEMESH_LIPS,
                    mp.solutions.face_mesh.FACEMESH_LEFT_EYE,
                    mp.solutions.face_mesh.FACEMESH_RIGHT_EYE,
                    mp.solutions.face_mesh.FACEMESH_LEFT_EYEBROW,
                    mp.solutions.face_mesh.FACEMESH_RIGHT_EYEBROW,
                    mp.solutions.face_mesh.FACEMESH_NOSE
                ]
                xs, ys = [], []
                for region in key_regions:
                    for connection in region:
                        idx1, idx2 = connection
                        if idx1 < len(landmarks) and idx2 < len(landmarks):
                            xs.extend([landmarks[idx1].x, landmarks[idx2].x])
                            ys.extend([landmarks[idx1].y, landmarks[idx2].y])
                if xs and ys:
                    x1, x2 = int(min(xs) * w), int(max(xs) * w)
                    y1, y2 = int(min(ys) * h), int(max(ys) * h)
                    padding = 5
                    x1, y1 = max(x1 - padding, 0), max(y1 - padding, 0)
                    x2, y2 = min(x2 + padding, w), min(y2 + padding, h)
                    side = max(x2 - x1, y2 - y1)
                    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                    x1, y1 = max(cx - side // 2, 0), max(cy - side // 2, 0)
                    x2, y2 = min(x1 + side, w), min(y1 + side, h)
                    if y1 < y2 and x1 < x2:
                        roi = frame[y1:y2, x1:x2]
                        return cv2.resize(roi, COMMON_SIZE, interpolation=cv2.INTER_AREA)
                logging.warning("⚠️ No valid face ROI detected.")
            except Exception as e:
                logging.error(f"❌ Error extracting face ROI: {e}")
        elif hand_landmarks is not None:
            try:
                landmarks = hand_landmarks.landmark if hasattr(hand_landmarks, "landmark") else hand_landmarks
                xs = [lm.x for lm in landmarks]
                ys = [lm.y for lm in landmarks]
                if xs and ys:
                    x1, x2 = int(min(xs) * w), int(max(xs) * w)
                    y1, y2 = int(min(ys) * h), int(max(ys) * h)
                    padding = 10
                    x1, y1 = max(x1 - padding, 0), max(y1 - padding, 0)
                    x2, y2 = min(x2 + padding, w), min(y2 + padding, h)
                    side = max(x2 - x1, y2 - y1)
                    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                    x1, y1 = max(cx - side // 2, 0), max(cy - side // 2, 0)
                    x2, y2 = min(x1 + side, w), min(y1 + side, h)
                    if y1 < y2 and x1 < x2:
                        roi = frame[y1:y2, x1:x2]
                        return cv2.resize(roi, COMMON_SIZE, interpolation=cv2.INTER_AREA)
                logging.warning("⚠️ No valid hand ROI detected.")
            except Exception as e:
                logging.error(f"❌ Error extracting hand ROI: {e}")
        return None

    def compute_deepphys_rppg(self, roi_frames):
        """
        Computes rPPG signal using the DeepPhys model.
        Resizes ROI frames from (240,320) to (72,72) to match model input.
        Moves the input to GPU before inference.
        """
        # roi_frames: numpy array of shape (N, H, W, C)
        frames_tensor = torch.tensor(roi_frames, dtype=torch.float32) / 255.0  # Normalize pixels
        frames_tensor = frames_tensor.permute(0, 3, 1, 2)  # Shape: (N, C, H, W)
        # Resize frames to (72, 72)
        frames_tensor = torch.nn.functional.interpolate(frames_tensor, size=(72, 72), mode='bilinear', align_corners=False)
        # Compute motion branch (difference between consecutive frames)
        motion = torch.cat([torch.zeros_like(frames_tensor[:1]), frames_tensor[1:] - frames_tensor[:-1]], dim=0)
        # Create six-channel input: [motion | appearance]
        deepphys_input = torch.cat([motion, frames_tensor], dim=1)
        # Move input to GPU
        deepphys_input = deepphys_input.to(torch.device('cuda'))
        with torch.no_grad():
            outputs = self.deepphys_model(deepphys_input)
        return outputs.squeeze().cpu().numpy()




    def process_video(self, video_path):
        logging.warning(f"Processing video: {video_path}")
        # Reset buffers for a new video
        self.face_roi_buffer = []
        self.hand_roi_buffer = []
        
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            logging.error(f"Could not open {video_path}, skipping.")
            return (None, None, None, None, None, None, None)
        
        frame_idx = 0
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        video_fps = CONFIG["FS"]  # or simply 30
        if video_fps == 0 or frame_count == 0:
            logging.error(f"Invalid video FPS or frame count for {video_path}.")
            return (None, None, None, None, None, None, None)
        logging.warning(f"Video FPS: {video_fps}, Frames: {frame_count}")
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if frame_idx % self.sampling_factor != 0:
                frame_idx += 1
                continue

            frame_resized = cv2.resize(frame, (128, 128))
            # Compute timestamp based on frame index and fps:
            timestamp_ms = int((frame_idx / video_fps) * 1000)
            # Ensure timestamps are strictly increasing across videos:
            if timestamp_ms <= self.last_timestamp_ms:
                timestamp_ms = self.last_timestamp_ms + 1
            self.last_timestamp_ms = timestamp_ms

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            )
            try:
                face_results = self.face_landmarker_model.detect_for_video(mp_image, timestamp_ms)
                hand_results = self.hand_landmarker_model.detect_for_video(mp_image, timestamp_ms)
            except ValueError as e:
                logging.error(f"Frame {frame_idx} skipped due to timestamp error: {e}")
                frame_idx += 1
                continue

            face_landmarks = face_results.face_landmarks[0] if face_results and face_results.face_landmarks else None
            hand_landmarks = hand_results.hand_landmarks[0] if hand_results and hand_results.hand_landmarks else None

            if face_landmarks:
                roi_face = self.extract_roi(frame_resized, video_fps, face_landmarks=face_landmarks)
                if roi_face is not None:
                    self.face_roi_buffer.append(roi_face)
            if hand_landmarks:
                roi_hand = self.extract_roi(frame_resized, video_fps, hand_landmarks=hand_landmarks)
                if roi_hand is not None:
                    self.hand_roi_buffer.append(roi_hand)
            frame_idx += 1

        cap.release()
        gc.collect()

        if len(self.face_roi_buffer) < 20:
            logging.warning(f"Not enough face ROI frames for rPPG processing. Got {len(self.face_roi_buffer)}.")
            return (None, None, None, None, None, None, None)
        face_buffer_array = np.stack(self.face_roi_buffer, axis=0)
        logging.warning(f"Stacked face ROI array shape: {face_buffer_array.shape}")
      
        face_rppg = self.compute_deepphys_rppg(face_buffer_array)

        if face_rppg is None or np.prod(face_rppg.shape) == 0:
            logging.error("No valid rPPG signal extracted using DeepPhys.")
            return (None, None, None, None, None, None, None)
        logging.warning(f"Extracted face rPPG signal shape: {face_rppg.shape}")

        if len(self.hand_roi_buffer) >= 20:
            hand_buffer_array = np.stack(self.hand_roi_buffer, axis=0)
            hand_rppg = self.compute_deepphys_rppg(hand_buffer_array)
        else:
            hand_rppg = None

        if face_rppg is None or (hasattr(face_rppg, '__len__') and len(face_rppg) < 10):
            logging.warning("Not enough valid face rPPG data for vital sign processing.")
            heart_rate, spo2, respiration_rate = None, None, None
        else:
            heart_rate, spo2, respiration_rate = RPPGProcessor.process_rppg(face_rppg, video_fps)

        if hand_rppg is None or (hasattr(face_rppg, '__len__') and len(face_rppg) < 10):
            ptt_value, ptt_confidence = None, None
        else:
            ptt_value, ptt_confidence = PTTBPProcessor.compute_ptt(face_rppg, hand_rppg, video_fps)
            if ptt_value is not None:
                logging.info(f"Computed PTT: {ptt_value:.5f} sec (Confidence: {ptt_confidence:.3f})")

        sbp_value, dbp_value = PTTBPProcessor.estimate_bp(ptt_value) if ptt_value is not None else (None, None)
        if sbp_value and dbp_value:
            logging.info(f"Computed SBP: {sbp_value}, DBP: {dbp_value}")

        return (
            [sbp_value if sbp_value is not None else None],
            [dbp_value if dbp_value is not None else None],
            [ptt_value if ptt_value is not None else None],
            [face_rppg if face_rppg is not None else None],
            [heart_rate if heart_rate is not None else None],
            [spo2 if spo2 is not None else None],
            [respiration_rate if respiration_rate is not None else None]
        )
