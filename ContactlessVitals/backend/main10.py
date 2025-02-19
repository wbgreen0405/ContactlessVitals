import os
import logging
import pandas as pd
import numpy as np
from scipy.stats import boxcox
from scripts.video_processing import VideoProcessor  # Using the updated VideoProcessor
from scripts.ptt_bp_preprocessing import PTTBPProcessor

logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")

VIDEO_DIR = "/content/drive/MyDrive/Omdena-SonoCare/sonocare/V-BPE Dataset new copy/videos_input"
SAVE_DIR = "/content/drive/MyDrive/Omdena-SonoCare/POS_WANG/assets"
os.makedirs(SAVE_DIR, exist_ok=True)

def ensure_non_empty(lst):
    if lst is None or len(lst) == 0:
        return [np.nan]
    return lst

def extract_video_name(video_path):
    return os.path.splitext(os.path.basename(video_path))[0]

def apply_boxcox_transformation(values):
    try:
        values = np.asarray(values).astype(float)
        # Check if all values are (almost) equal:
        if np.allclose(values, values[0]):
            logging.warning("Data is constant. Skipping Box-Cox transformation.")
            return values
        values[values <= 0] = np.nan  # Box-Cox requires positive values
        if np.all(np.isnan(values)):
            logging.warning("All values are non-positive. Box-Cox transformation skipped.")
            return values
        transformed_values, _ = boxcox(values[~np.isnan(values)])
        values[~np.isnan(values)] = transformed_values
        return values
    except Exception as e:
        logging.error(f"Error applying Box-Cox transformation: {e}")
        return values  # Return original values if transformation fails

def process_all_videos(video_dir):
    video_processor = VideoProcessor()
    all_dfs = []

    # Use os.walk to process subfolders as well
    for root, dirs, files in os.walk(video_dir):
        for file in files:
            if file.lower().endswith(".mp4"):
                video_path = os.path.join(root, file)
                logging.warning(f"Processing video: {video_path}")
                result = video_processor.process_video(video_path)
                if result is None:
                    logging.warning(f"No valid data extracted from {video_path}. Skipping...")
                    continue

                sbp_values, dbp_values, ptt_values, rppg_values, heart_rates, spo2_values, respiration_rates = result

                # Use the global ensure_non_empty function
                sbp_values = ensure_non_empty(sbp_values)
                dbp_values = ensure_non_empty(dbp_values)
                ptt_values = ensure_non_empty(ptt_values)
                rppg_values = ensure_non_empty(rppg_values)
                heart_rates = ensure_non_empty(heart_rates)
                spo2_values = ensure_non_empty(spo2_values)
                respiration_rates = ensure_non_empty(respiration_rates)

                sbp_values = apply_boxcox_transformation(sbp_values)
                dbp_values = apply_boxcox_transformation(dbp_values)
                heart_rates = apply_boxcox_transformation(heart_rates)

                min_length = min(
                    len(sbp_values), len(dbp_values), len(ptt_values),
                    len(rppg_values), len(heart_rates), len(spo2_values), len(respiration_rates)
                )
                logging.warning(f"Trimming all lists to min_length={min_length}")

                subject_id = extract_video_name(video_path)
                df = pd.DataFrame({
                    "Subject_ID": [subject_id] * min_length,
                    "Frame": np.arange(min_length),
                    "PTT": ptt_values[:min_length],
                    "rPPG": rppg_values[:min_length],
                    "SBP": sbp_values[:min_length],
                    "DBP": dbp_values[:min_length],
                    "Heart_Rate": heart_rates[:min_length],
                    "SpO2": spo2_values[:min_length],
                    "Respiration_Rate": respiration_rates[:min_length]
                })

                if df.empty:
                    logging.warning(f"DataFrame is empty for {video_path}. Skipping.")
                    continue

                logging.warning(f"Processed data for {subject_id} has {len(df)} rows.")
                all_dfs.append(df)

    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        combined_save_path = os.path.join(SAVE_DIR, "combined_processed_videos.csv")
        combined_df.to_csv(combined_save_path, index=False)
        logging.warning(f"Combined processed data saved: {combined_save_path}")
        return combined_df
    else:
        logging.warning("No valid data extracted from any videos.")
        return None

def main():
    logging.warning(f"Starting processing of videos in {VIDEO_DIR}")
    df = process_all_videos(VIDEO_DIR)
    if df is None or df.empty:
        logging.warning("Processing failed. No data extracted.")
    else:
        logging.warning(f"Processing complete. Combined data has {len(df)} rows.")

if __name__ == "__main__":
    main()

