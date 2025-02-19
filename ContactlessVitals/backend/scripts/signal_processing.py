from scipy import signal, sparse
from scipy.signal import detrend
import numpy as np
import logging
import time

# Configure Logging (Set to INFO to suppress debug messages)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class SignalProcessor:
    """Class for handling signal processing operations"""



    import time

    @staticmethod
    def detect_outliers(signal_data, threshold=3.0):
        if signal_data is None or len(signal_data) < 5:
            logging.warning("⚠️ Insufficient data for outlier detection.")
            return signal_data

        start_time = time.time()
        signal_data = np.asarray(signal_data).flatten()
        mean_val = np.mean(signal_data)
        std_val = np.std(signal_data)
        z_scores = (signal_data - mean_val) / (std_val + 1e-6)
        
        outlier_mask = np.abs(z_scores) > threshold
        num_outliers = np.sum(outlier_mask)
        
        if num_outliers > 0:
            logging.info(f"🔍 Detected {num_outliers} outliers. Applying correction...")
            indices = np.arange(len(signal_data))
            valid_mask = ~outlier_mask
            signal_data = np.interp(indices, indices[valid_mask], signal_data[valid_mask])
        end_time = time.time()
        logging.info(f"⏱ Outlier detection and correction took {end_time - start_time:.2f} seconds.")
        return signal_data


    @staticmethod
    def detect_outliers2(signal_data, threshold=3.0):
        """
        Detects and removes outliers from the rPPG signal using a Z-score threshold.
        Values with a Z-score above `threshold` are considered outliers.
        
        Args:
            signal_data (numpy array): Input rPPG signal.
            threshold (float): Z-score threshold for outlier detection.
        
        Returns:
            numpy array: Cleaned rPPG signal with outliers replaced by interpolation.
        """
        if signal_data is None or len(signal_data) < 5:
            logging.warning("⚠️ Insufficient data for outlier detection.")
            return signal_data

        signal_data = np.asarray(signal_data).flatten()
        mean_val = np.mean(signal_data)
        std_val = np.std(signal_data)
        z_scores = (signal_data - mean_val) / (std_val + 1e-6)  # Avoid division by zero
        
        # Identify outliers
        outlier_mask = np.abs(z_scores) > threshold
        num_outliers = np.sum(outlier_mask)

        if num_outliers > 0:
            logging.info(f"🔍 Detected {num_outliers} outliers in rPPG signal. Applying correction...")

            # Replace outliers with interpolated values
            indices = np.arange(len(signal_data))
            valid_mask = ~outlier_mask
            interp_func = np.interp(indices, indices[valid_mask], signal_data[valid_mask])
            signal_data = interp_func

        return signal_data

    @staticmethod
    def median_filter(signal_data, window_size=5):
        """
        Applies a rolling median filter to suppress sudden spikes in rPPG signals.
        
        Args:
            signal_data (numpy array): Input rPPG signal.
            window_size (int): The window size for median filtering.
        
        Returns:
            numpy array: Smoothed rPPG signal.
        """
        if signal_data is None or len(signal_data) < window_size:
            return signal_data

        return signal.medfilt(signal_data, kernel_size=window_size)

    @staticmethod
    def detrend(input_signal):
        """
        Removes the linear trend from the rPPG signal using scipy's detrend.
        
        Args:
            input_signal (numpy array): Input rPPG signal.
        
        Returns:
            numpy array: Detrended signal.
        """
        if input_signal is None or np.asarray(input_signal).size < 5:
            logging.warning("⚠️ Insufficient data for detrending.")
            return input_signal
        try:
            return detrend(input_signal)
        except Exception as e:
            logging.error(f"❌ ERROR in detrend(): {e}")
            return None

    @staticmethod
    def detrend2(input_signal, lambda_value=100):
        """
        Applies a detrending filter to remove slow fluctuations from the rPPG signal.
        
        Args:
            input_signal (numpy array): Input rPPG signal.
            lambda_value (float): Smoothing factor.
        
        Returns:
            numpy array: Detrended rPPG signal.
        """
        if input_signal is None or len(input_signal) < 5:
            logging.warning("⚠️ Insufficient data for detrending.")
            return input_signal

        signal_length = len(input_signal)
        H = np.identity(signal_length)
        ones = np.ones(signal_length)
        minus_twos = -2 * np.ones(signal_length)
        diags_data = np.array([ones, minus_twos, ones])
        diags_index = np.array([0, 1, 2])
        D = sparse.spdiags(diags_data, diags_index, (signal_length - 2), signal_length).toarray()

        try:
            detrended_signal = np.dot(
                (H - np.linalg.inv(H + (lambda_value ** 2) * np.dot(D.T, D))), input_signal
            )
            return detrended_signal
        except Exception as e:
            logging.error(f"❌ ERROR in detrend(): {e}")
            return None

    

    @staticmethod
    def preprocess_rppg(signal_data):
        """
        Applies a full preprocessing pipeline:
        - Removes outliers
        - Applies a median filter
        - Detrends the signal

        Args:
            signal_data (numpy array): Input rPPG signal.

        Returns:
            numpy array: Preprocessed rPPG signal.
        """
        if signal_data is None or np.asarray(signal_data).size < 5:
            logging.warning("⚠️ Insufficient data for preprocessing.")
            return None

        # Flatten, then process the signal.
        signal_data = np.asarray(signal_data).flatten()
        signal_data = SignalProcessor.detect_outliers(signal_data)
        signal_data = SignalProcessor.median_filter(signal_data)
        signal_data = SignalProcessor.detrend(signal_data)

        if signal_data is None:
            logging.warning("⚠️ Preprocessing failed during detrending.")
            return None

        logging.info(f"✅ Preprocessing complete. Final Signal Length: {len(signal_data)}")
        return signal_data
