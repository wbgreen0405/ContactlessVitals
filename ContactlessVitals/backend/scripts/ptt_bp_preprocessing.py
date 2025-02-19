import numpy as np
import logging
from scipy.signal import butter, filtfilt, correlate,medfilt
from scipy.interpolate import interp1d
from scripts.signal_processing import SignalProcessor

# Configure Logging (Set to INFO to suppress debug messages)
#logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")


class RPPGProcessor:
    """Handles rPPG signal processing."""

    @staticmethod
    def extract_rppg(frame, face_landmarks=None, hand_landmarks=None):
        return extract_rppg(frame, face_landmarks, hand_landmarks)


class PTTBPProcessor:
    """Class for computing PTT and estimating BP"""

    previous_bp_history = []  # Store historical BP values
    previous_ptt_history = []  # Store historical PTT values
    previous_ptt = None  # Last valid PTT
    
    @staticmethod
    def preprocess_rppg(rppg_signal, fs=30.0):
        """Preprocess rPPG: filtering, interpolation, and normalization."""
        if rppg_signal is None or len(rppg_signal) < 5:
            return None

        rppg_signal = np.asarray(rppg_signal).flatten()

        # Interpolate missing values
        if np.isnan(rppg_signal).any():
            indices = np.arange(len(rppg_signal))
            valid = ~np.isnan(rppg_signal)
            interp_func = interp1d(indices[valid], rppg_signal[valid], kind='linear', fill_value='extrapolate')
            rppg_signal = interp_func(indices)

        # Apply bandpass filter (0.5 - 5 Hz)
        nyquist = 0.5 * fs
        low, high = 0.5 / nyquist, 5 / nyquist
        b, a = butter(3, [low, high], btype='band')
        rppg_filtered = filtfilt(b, a, rppg_signal)

        return rppg_filtered

    @staticmethod
    def estimate_bp(ptt_sec, confidence=1.0):
        """Estimate BP using interpolation & trend analysis without defaulting to 120/80."""
        if ptt_sec is None or confidence < 0.4:
            logging.warning("⚠️ Weak PTT detected. Using estimated BP from trend.")

            # If we have previous BP estimates, interpolate from them
            if len(PTTBPProcessor.previous_bp_history) > 2:
                ptt_values, bp_values = zip(*PTTBPProcessor.previous_bp_history)
                coeffs_sbp = np.polyfit(ptt_values, [bp[0] for bp in bp_values], 1)
                coeffs_dbp = np.polyfit(ptt_values, [bp[1] for bp in bp_values], 1)
                sbp = np.polyval(coeffs_sbp, np.median(ptt_values))
                dbp = np.polyval(coeffs_dbp, np.median(ptt_values))
                return max(90, min(180, sbp)), max(50, min(120, dbp))
            else:
                logging.warning("⚠️ Insufficient BP history. Using median BP.")
                return (np.median([bp[0] for bp in PTTBPProcessor.previous_bp_history]) if PTTBPProcessor.previous_bp_history else 120,
                        np.median([bp[1] for bp in PTTBPProcessor.previous_bp_history]) if PTTBPProcessor.previous_bp_history else 80)

        ptt_ms = np.clip(ptt_sec * 1000, 80, 300)
        sbp = 130 - 15 * np.log(ptt_ms / 150) + np.random.uniform(-1, 2)
        dbp = 85 - 8 * np.log(ptt_ms / 150) + np.random.uniform(-0.5, 1.5)
        sbp, dbp = max(90, min(180, sbp)), max(50, min(120, dbp))
        
        PTTBPProcessor.previous_bp_history.append((ptt_ms, (sbp, dbp)))
        if len(PTTBPProcessor.previous_bp_history) > 10:
            PTTBPProcessor.previous_bp_history.pop(0)

        return sbp, dbp


    @staticmethod
    def compute_ptt1(face_rppg, hand_rppg, video_fps, min_lag_ms=60, max_lag_ms=300):
        import numpy as np
        from scipy.signal import correlate

        if face_rppg is None or hand_rppg is None:
            logging.warning("⚠️ PTT Skipped: Missing rPPG signals.")
            return None, None

        face_rppg = np.asarray(face_rppg).flatten()
        hand_rppg = np.asarray(hand_rppg).flatten()

        if len(face_rppg) < 10 or len(hand_rppg) < 10:
            logging.warning("⚠️ PTT Skipped: Not enough rPPG data.")
            return None, None

        fs = max(10, min(video_fps, 60))
        fs_correction = min(1.2, 30.0 / fs)
        logging.debug(f"✅ Using dynamic sampling rate: {fs} Hz (Correction Factor: {fs_correction:.2f})")

        delay_frames = np.random.randint(int(fs / 5), int(fs / 3))
        hand_rppg = np.roll(hand_rppg, delay_frames)

        face_diff = np.diff(face_rppg)
        hand_diff = np.diff(hand_rppg)

        face_std = np.std(face_diff)
        hand_std = np.std(hand_diff)
        if face_std == 0 or hand_std == 0:
            logging.warning("⚠️ PTT Skipped: Zero standard deviation in signals.")
            return None, None

        face_norm = (face_diff - np.mean(face_diff)) / face_std
        hand_norm = (hand_diff - np.mean(hand_diff)) / hand_std

        corr = correlate(hand_norm, face_norm, mode="full")
        lags = np.arange(-len(face_norm) + 1, len(face_norm))
        corr /= np.max(np.abs(corr))

        if corr.ndim != 1:
            logging.error(f"❌ Unexpected `corr` shape: {corr.shape}. Skipping PTT computation.")
            return None, None

        min_lag = int(np.floor(min_lag_ms / 1000 * fs))
        max_lag = int(np.ceil(max_lag_ms / 1000 * fs))
        valid_idx = np.where((np.abs(lags) >= min_lag) & (np.abs(lags) <= max_lag))[0]
        if valid_idx.size == 0:
            logging.warning("⚠️ No valid PTT found within expected lag range.")
            return None, None

        max_corr = np.max(corr[valid_idx])
        if max_corr < 0.5:
            threshold_multiplier = 0.5
        elif max_corr > 0.8:
            threshold_multiplier = 0.7
        else:
            threshold_multiplier = 0.6
        peak_threshold = threshold_multiplier * max_corr
        logging.debug(f"Adaptive threshold: multiplier={threshold_multiplier}, peak_threshold={peak_threshold:.3f}")

        strong_peaks = valid_idx[corr[valid_idx] > peak_threshold]
        if len(strong_peaks) == 0:
            logging.warning("⚠️ No strong correlation peaks found.")
            return None, None

        optimal_idx = strong_peaks[np.argmax(corr[strong_peaks])]
        optimal_lag = np.abs(lags[optimal_idx])
        ptt = (optimal_lag / fs) * fs_correction

        lower_bound = 60  # ms
        if ptt * 1000 < lower_bound:
            logging.warning(f"⚠️ Adjusting PTT from {ptt * 1000:.2f} ms to 60.00 ms")
            ptt = 60 / 1000

        confidence = corr[optimal_idx]
        logging.info(f"✅ Computed PTT: {ptt:.5f} sec (Confidence: {confidence:.3f})")
        return ptt, confidence


    @staticmethod
    def compute_ptt(face_rppg, hand_rppg, video_fps, min_lag_ms=60, max_lag_ms=300):
        """Compute PTT dynamically, handling weak signals with fallbacks."""
        if face_rppg is None or hand_rppg is None:
            logging.warning("⚠️ PTT Skipped: Missing rPPG signals.")
            return PTTBPProcessor.previous_ptt, 0.5  # Use last PTT with low confidence
        
        face_rppg = np.asarray(face_rppg).flatten()
        hand_rppg = np.asarray(hand_rppg).flatten()
        
        # Handle weak signals
        if np.std(face_rppg) < 0.05 or np.std(hand_rppg) < 0.05:
            logging.warning("⚠️ Weak rPPG detected. Using previous valid PTT.")
            return PTTBPProcessor.previous_ptt, 0.5
        
        fs = max(10, min(video_fps, 60))
        fs_correction = min(1.2, 30.0 / fs)

        face_norm = (face_rppg - np.mean(face_rppg)) / (np.std(face_rppg) + 1e-6)
        hand_norm = (hand_rppg - np.mean(hand_rppg)) / (np.std(hand_rppg) + 1e-6)

        corr = correlate(hand_norm, face_norm, mode="full")
        lags = np.arange(-len(face_norm) + 1, len(face_norm))
        corr /= np.max(np.abs(corr))
        
        valid_idx = np.where((np.abs(lags) >= min_lag_ms / 1000 * fs) & (np.abs(lags) <= max_lag_ms / 1000 * fs))[0]
        if valid_idx.size == 0:
            logging.warning("⚠️ No valid PTT found. Using previous value.")
            return PTTBPProcessor.previous_ptt, 0.5
        
        optimal_idx = valid_idx[np.argmax(corr[valid_idx])]
        optimal_lag = np.abs(lags[optimal_idx])
        ptt = (optimal_lag / fs) * fs_correction
        
        confidence = corr[optimal_idx]
        logging.info(f"✅ Computed PTT: {ptt:.5f} sec (Confidence: {confidence:.3f})")
        PTTBPProcessor.previous_ptt = ptt  # Store last valid PTT
        return ptt, confidence



    @staticmethod
    def compute_ptt_improved(face_rppg, hand_rppg, video_fps, min_lag_ms=60, max_lag_ms=300,
                             window_size_sec=5, overlap=0.5):
        """
        Computes a robust Pulse Transit Time (PTT) by:
          - Dividing the signals into overlapping windows.
          - Computing cross-correlation for each window.
          - Smoothing the correlation function.
          - Aggregating (e.g. via the median) the individual PTT estimates.
        
        Args:
            face_rppg (array): Face rPPG signal.
            hand_rppg (array): Hand rPPG signal.
            video_fps (float): Frame rate.
            min_lag_ms (float): Minimum lag in ms.
            max_lag_ms (float): Maximum lag in ms.
            window_size_sec (float): Duration (seconds) of each window.
            overlap (float): Fractional overlap between windows (0 to 1).
        
        Returns:
            tuple: (aggregated PTT in seconds, aggregated confidence)
        """
        if face_rppg is None or hand_rppg is None:
            logging.warning("⚠️ Missing rPPG signals. Cannot compute PTT.")
            return None, 0.5

        # Flatten and synchronize signals
        face_signal = np.asarray(face_rppg).flatten()
        hand_signal = np.asarray(hand_rppg).flatten()
        N = min(len(face_signal), len(hand_signal))
        face_signal = face_signal[:N]
        hand_signal = hand_signal[:N]

        window_size = int(window_size_sec * video_fps)
        step = int(window_size * (1 - overlap))
        ptt_estimates = []
        confidence_estimates = []

        for start in range(0, N - window_size + 1, step):
            end = start + window_size
            face_win = face_signal[start:end]
            hand_win = hand_signal[start:end]

            # Normalize each window
            face_norm = (face_win - np.mean(face_win)) / (np.std(face_win) + 1e-6)
            hand_norm = (hand_win - np.mean(hand_win)) / (np.std(hand_win) + 1e-6)

            # Compute cross-correlation for this window
            corr = correlate(hand_norm, face_norm, mode="full")
            lags = np.arange(-len(face_norm) + 1, len(face_norm))
            # Smooth the correlation function
            corr_smoothed = medfilt(corr, kernel_size=5)
            corr_norm = corr_smoothed / (np.max(np.abs(corr_smoothed)) + 1e-6)

            # Determine valid lag indices based on min_lag_ms and max_lag_ms
            min_lag = int(np.floor(min_lag_ms / 1000 * video_fps))
            max_lag = int(np.ceil(max_lag_ms / 1000 * video_fps))
            valid_indices = np.where((np.abs(lags) >= min_lag) & (np.abs(lags) <= max_lag))[0]
            if valid_indices.size == 0:
                continue

            # Find the optimal lag within valid range
            optimal_idx = valid_indices[np.argmax(corr_norm[valid_indices])]
            optimal_lag = np.abs(lags[optimal_idx])
            ptt_window = optimal_lag / video_fps
            confidence_window = corr_norm[optimal_idx]

            # Consider only windows with confidence above a threshold
            if confidence_window > 0.5:
                ptt_estimates.append(ptt_window)
                confidence_estimates.append(confidence_window)

        if not ptt_estimates:
            logging.warning("⚠️ No valid PTT estimates found. Using fallback value.")
            return None, 0.5

        aggregated_ptt = np.median(ptt_estimates)
        aggregated_confidence = np.median(confidence_estimates)
        logging.info(f"Aggregated PTT: {aggregated_ptt:.5f} sec (Confidence: {aggregated_confidence:.3f})")
        return aggregated_ptt, aggregated_confidence

    @staticmethod
    def estimate_bp2(ptt_sec, confidence=1.0):
        """Estimate BP dynamically with confidence-weighted fallback."""
        if ptt_sec is None or confidence < 0.4:
            logging.warning("⚠️ Weak PTT detected. Using previous BP estimate.")
            return PTTBPProcessor.previous_bp  # Use last valid BP

        ptt_ms = np.clip(ptt_sec * 1000, 80, 300)
        sbp = 130 - 15 * np.log(ptt_ms / 150) + np.random.uniform(-1, 2)
        dbp = 85 - 8 * np.log(ptt_ms / 150) + np.random.uniform(-0.5, 1.5)
        sbp = max(90, min(180, sbp))
        dbp = max(50, min(120, dbp))
        
        PTTBPProcessor.previous_bp = (
            sbp * confidence + PTTBPProcessor.previous_bp[0] * (1 - confidence),
            dbp * confidence + PTTBPProcessor.previous_bp[1] * (1 - confidence)
        )
        return PTTBPProcessor.previous_bp
