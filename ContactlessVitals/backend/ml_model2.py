import os
import ast
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, RandomizedSearchCV, KFold
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

def merge_datasets(combined_path, metadata_path, output_path):
    """
    Merges the processed video dataset with metadata and saves the result.
    """
    combined_df = pd.read_csv(combined_path)
    metadata_df = pd.read_csv(metadata_path)
    
    # Clean Subject_ID column
    combined_df['Subject_ID'] = combined_df['Subject_ID'].str.replace('Copy of ', '', regex=False)
    
    # Merge DataFrames
    merged_df = pd.merge(combined_df, metadata_df, left_on='Subject_ID', right_on='ID', how='inner')
    
    # Save merged dataset
    merged_df.to_csv(output_path, index=False)
    print(f"Merged dataset saved to: {output_path}")
    return merged_df

def train_model(dataset_path, save_dir, assets_dir):
    """
    Loads dataset, preprocesses data, trains a stacked regression model, and saves the results.
    """
    os.makedirs(save_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)
    
    # Load dataset
    df = pd.read_csv(dataset_path)
    computed_features = ['PTT', 'rPPG', 'SBP', 'DBP', 'Heart_Rate', 'SpO2_x', 'Respiration_Rate']
    ground_truth = ['BPS', 'BPD', 'Pulse']
    df = df.dropna(subset=[col for col in computed_features + ground_truth if col != 'rPPG'])
    
    # Process rPPG feature
    def process_rppg_feature(x):
        try:
            arr = np.array(ast.literal_eval(x))
            return pd.Series({'rPPG_mean': np.mean(arr), 'rPPG_std': np.std(arr)})
        except Exception:
            return pd.Series({'rPPG_mean': np.nan, 'rPPG_std': np.nan})
    
    if df['rPPG'].dtype == object:
        rppg_features = df['rPPG'].apply(process_rppg_feature)
        df = df.drop(columns=['rPPG'])
        df = pd.concat([df, rppg_features], axis=1)
        computed_features.remove('rPPG')
        computed_features.extend(['rPPG_mean', 'rPPG_std'])
    
    df[computed_features] = df[computed_features].fillna(0)
    
    X = df[computed_features]
    y = df[ground_truth]
    
    # Feature Engineering
    feature_engineering = ColumnTransformer([
        ("num", StandardScaler(), computed_features),
        ("poly", PolynomialFeatures(degree=2, interaction_only=True), computed_features)
    ])
    
    # Model setup
    base_estimators = [
        ("rf", RandomForestRegressor(n_estimators=200, max_depth=10, min_samples_split=5, random_state=42)),
        ("gbr", GradientBoostingRegressor(n_estimators=200, max_depth=10, min_samples_split=5, random_state=42)),
    ]
    
    stacking_reg = StackingRegressor(
        estimators=base_estimators,
        final_estimator=GradientBoostingRegressor(loss='quantile', alpha=0.75, n_estimators=200, max_depth=5),
        cv=5,
        passthrough=True
    )
    
    ensemble_model = MultiOutputRegressor(stacking_reg)
    
    pipeline = Pipeline([
        ("preprocessor", feature_engineering),
        ("regressor", ensemble_model)
    ])
    
    # Hyperparameter tuning
    param_grid = {
        "regressor__estimator__rf__n_estimators": [50, 100, 200],
        "regressor__estimator__gbr__n_estimators": [50, 100, 200],
        "regressor__estimator__rf__max_depth": [None, 5, 10],
        "regressor__estimator__gbr__max_depth": [None, 5, 10],
        "regressor__estimator__rf__min_samples_split": [2, 5, 10],
    }
    
    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    random_search = RandomizedSearchCV(pipeline, param_grid, cv=cv, scoring="neg_mean_squared_error", n_iter=20, n_jobs=-1, random_state=42)
    random_search.fit(X, y)
    
    print("Best hyperparameters:", random_search.best_params_)
    best_model = random_search.best_estimator_
    
    # Specify one input per feature column
    initial_type = [(name, FloatTensorType([None, 1])) for name in computed_features]
    onnx_model = convert_sklearn(best_model, initial_types=initial_type)
    onnx_path = os.path.join(save_dir, "calibration_ensemble_model.onnx")
    with open(onnx_path, "wb") as f:
        f.write(onnx_model.SerializeToString())
    print(f"ONNX ensemble model saved to {onnx_path}")

if __name__ == "__main__":
    # Define paths
    combined_data_path = "/path/to/combined_processed_videos.csv"
    metadata_data_path = "/path/to/Demographic_Data.csv"
    merged_output_path = "/path/to/merged_videos.csv"

    # Merge datasets
    merged_df = merge_datasets(combined_data_path, metadata_data_path, merged_output_path)

    # Define paths for training
    save_directory = "/path/to/save_models/"
    assets_directory = "/path/to/save_assets/"

    # Train the model
    train_model(merged_output_path, save_directory, assets_directory)

