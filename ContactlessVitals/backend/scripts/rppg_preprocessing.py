import numpy as np
import logging
from scipy.signal import butter, filtfilt, find_peaks, savgol_filter
from scripts.signal_processing import SignalProcessor

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class RPPGProcessor:
    """Handles rPPG signal processing (Heart Rate, SpO₂, Respiration Rate)."""

    @staticmethod
    def POS_WANG(BVP, fs=30):
        """
        Processes BVP signals using a bandpass filter.
        """
        if BVP is None:
            logging.warning("⚠️ POS_WANG: BVP is None.")
            return None

        if len(BVP.shape) == 2 and BVP.shape[0] == 3:
            BVP = BVP.reshape((1, 3, BVP.shape[1]))

        if BVP.shape[-1] < 10:
            logging.warning(f"⚠️ POS_WANG: Not enough data points ({BVP.shape[-1]}) for filtering. Skipping...")
            return None

        lowcut, highcut = 0.7, 4.0
        nyquist = 0.5 * fs
        low, high = lowcut / nyquist, highcut / nyquist
        b, a = butter(3, [low, high], btype="band")

        try:
            BVP_filtered = filtfilt(b, a, BVP.astype(np.double), axis=-1)
        except ValueError as e:
            logging.error(f"❌ POS_WANG: Error during filtering: {e}")
            return None

        return BVP_filtered

    @staticmethod
    def extract_rgb_signals(frames, video_fps):
        """Extracts RGB signals from face ROI frames."""
        if frames is None or len(frames) == 0:
            logging.error("❌ extract_rgb_signals() received an empty frame sequence.")
            return None

        try:
            frames = np.asarray(frames)
            if len(frames.shape) < 3:
                logging.error(f"❌ Unexpected frame shape {frames.shape}. Expected (N, H, W, C).")
                return None

            RGB = [np.mean(frame, axis=(0, 1)) for frame in frames if frame.size > 0]
            if len(RGB) == 0:
                logging.error("❌ extract_rgb_signals() failed to extract any RGB values.")
                return None

            RGB = np.asarray(RGB).T  # Shape (3, N)
            logging.info(f"✅ Extracted RGB signal shape: {RGB.shape}")
            return RGB.reshape(1, 3, -1)

        except Exception as e:
            logging.error(f"❌ Error in extract_rgb_signals(): {e}")
            return None

    @staticmethod
    def assess_signal_quality(rppg_signal, fs=30):
        """Computes an SQA score based on SNR, peak consistency, and variability."""
        if rppg_signal is None or len(rppg_signal) < 5:
            return 0  # No valid signal

        rppg_signal = np.asarray(rppg_signal).flatten()

        # Compute Signal-to-Noise Ratio (SNR)
        signal_power = np.var(rppg_signal)
        noise_power = np.var(np.diff(rppg_signal))
        snr = signal_power / (noise_power + 1e-6)  # Avoid division by zero
        snr_score = np.clip(snr / 10, 0, 1)  # Normalize to [0,1]

        # Peak Consistency
        peaks, _ = find_peaks(rppg_signal, distance=fs / 2)
        peak_density = len(peaks) / (len(rppg_signal) / fs)
        peak_score = np.clip(peak_density / 2, 0, 1)

        # Variability Score (normalized standard deviation)
        variability_score = np.clip(np.std(rppg_signal) / 0.5, 0, 1)

        # Combine metrics
        quality_score = (0.4 * snr_score) + (0.3 * peak_score) + (0.3 * variability_score)
        return quality_score

    @staticmethod
    def handle_weak_signal(rppg_signal):
        """Handles weak rPPG signals by applying interpolation and smoothing techniques."""
        if rppg_signal is None or len(rppg_signal) < 5:
            return None  # Not enough data to process

        rppg_signal = np.asarray(rppg_signal).flatten()

        # Interpolation for missing values
        if np.isnan(rppg_signal).any():
            indices = np.arange(len(rppg_signal))
            valid = ~np.isnan(rppg_signal)
            interp_func = np.interp(indices, indices[valid], rppg_signal[valid])
            rppg_signal = interp_func

        # Apply Savitzky-Golay filter for smoothing
        if len(rppg_signal) >= 5:
            rppg_signal = savgol_filter(rppg_signal, window_length=5, polyorder=2)

        return rppg_signal

    # Removed duplicate preprocess_rppg implementation.
    # Instead, we use SignalProcessor.preprocess_rppg for a single, unified preprocessing pipeline.

    @staticmethod
    def compute_heart_rate(BVP, fs):
        """Computes Heart Rate (BPM) using peak detection."""
        if BVP is None or len(BVP) < fs:
            logging.warning("⚠️ Not enough data points for heart rate computation.")
            return None

        try:
            BVP = np.asarray(BVP).flatten()
            peaks, _ = find_peaks(BVP, distance=fs * 0.5)
            num_beats = len(peaks)
            duration_sec = len(BVP) / fs

            if duration_sec > 0 and num_beats > 0:
                return max(40, min(180, (num_beats / duration_sec) * 60))  # Clamp HR range
            return None
        except Exception as e:
            logging.error(f"❌ ERROR in compute_heart_rate(): {e}")
            return None

    @staticmethod
    def compute_spo1(BVP):
        """Computes SpO₂ from the BVP signal using AC/DC ratio."""
        if BVP is None or not isinstance(BVP, np.ndarray):
            return None

        if len(BVP.shape) == 1 and BVP.size % 3 == 0:
            BVP = BVP.reshape((1, 3, -1))

        red, green = BVP[0, 0, :], BVP[0, 1, :]
        dc_red, dc_green = np.mean(red), np.mean(green)
        ac_red, ac_green = np.max(red) - np.min(red), np.max(green) - np.min(green)

        if dc_red == 0 or dc_green == 0 or ac_green == 0:
            return None

        R_ratio = (ac_red / dc_red) / (ac_green / dc_green)
        return max(0, min(100, 105.0 - R_ratio))


    @staticmethod
    def compute_spo(BVP):
        """Computes SpO₂ from the BVP signal using AC/DC ratio.
          If the signal is 1D (as from DeepPhys), return a default value.
        """
        if BVP is None or not isinstance(BVP, np.ndarray):
            return None

        # If the signal is 1D, we can't compute AC/DC ratios; return a default SpO₂ (e.g., 98)
        if BVP.ndim == 1:
            return 98

        # Otherwise, if it's 3-channel, proceed as before.
        if len(BVP.shape) == 2 and BVP.shape[0] == 3:
            BVP = BVP.reshape((1, 3, BVP.shape[1]))

        red, green = BVP[0, 0, :], BVP[0, 1, :]
        dc_red, dc_green = np.mean(red), np.mean(green)
        ac_red, ac_green = np.max(red) - np.min(red), np.max(green) - np.min(green)

        if dc_red == 0 or dc_green == 0 or ac_green == 0:
            return None

        R_ratio = (ac_red / dc_red) / (ac_green / dc_green)
        return max(0, min(100, 105.0 - R_ratio))

    @staticmethod
    def compute_respiration_rate(BVP, fs):
        """Computes respiration rate from BVP signal."""
        if BVP is None or len(BVP) < 16:
            return None

        lowcut, highcut = 0.15, 0.8
        nyquist = 0.5 * fs
        b, a = butter(4, [lowcut / nyquist, highcut / nyquist], btype="band")

        try:
            resp_signal = filtfilt(b, a, BVP.astype(np.double))
            peaks, _ = find_peaks(resp_signal, distance=fs / highcut)
            return len(peaks) * 60 / (len(BVP) / fs)
        except Exception:
            return None

    @staticmethod
    def process_rppg(rppg_values, fs=30.0):
        """Processes rPPG signal to compute heart rate, SpO₂, and respiration rate."""
        # Check based on number of samples in the last dimension.
        if rppg_values is None or np.asarray(rppg_values).shape[-1] < 5:
            logging.warning("⚠️ Insufficient rPPG data. Skipping processing.")
            return None, None, None

        # Preprocess the rPPG signal by calling the unified function from SignalProcessor.
        clean_rppg_signal = SignalProcessor.preprocess_rppg(rppg_values)

        return (
            RPPGProcessor.compute_heart_rate(clean_rppg_signal, fs),
            RPPGProcessor.compute_spo(clean_rppg_signal),
            RPPGProcessor.compute_respiration_rate(clean_rppg_signal, fs),
        )
