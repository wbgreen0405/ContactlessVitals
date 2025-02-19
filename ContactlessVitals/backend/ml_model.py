import os
import ast
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# --- Load Calibration Data ---
df = pd.read_csv(CALIBRATION_DATASET_PATH)
computed_features = ['PTT', 'rPPG', 'SBP', 'DBP', 'Heart_Rate', 'SpO2_x', 'Respiration_Rate']
ground_truth = ['BPS', 'BPD', 'Pulse']

df = df.dropna(subset=[col for col in computed_features + ground_truth if col != 'rPPG'])

# Process rPPG Feature
def process_rppg_feature(x):
    try:
        arr = np.array(ast.literal_eval(x))
        return pd.Series({'rPPG_mean': np.mean(arr), 'rPPG_std': np.std(arr)})
    except Exception as e:
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

# --- Feature Engineering: Add Polynomial Features ---
feature_engineering = ColumnTransformer([
    ("num", StandardScaler(), computed_features),
    ("poly", PolynomialFeatures(degree=2, interaction_only=True), computed_features)
])

# --- Stacking Regressor with Gradient Boosting as Final Estimator ---
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

# --- Improved Hyperparameter Tuning with RandomizedSearchCV ---
param_grid = {
    "regressor__estimator__rf__n_estimators": [50, 100, 200],
    "regressor__estimator__gbr__n_estimators": [50, 100, 200],
    "regressor__estimator__rf__max_depth": [None, 5, 10],
    "regressor__estimator__gbr__max_depth": [None, 5, 10],
    "regressor__estimator__rf__min_samples_split": [2, 5, 10],
}

from sklearn.model_selection import KFold

cv = KFold(n_splits=5, shuffle=True, random_state=42)  # Use KFold instead of StratifiedKFold
random_search = RandomizedSearchCV(pipeline, param_grid, cv=cv, scoring="neg_mean_squared_error", n_iter=20, n_jobs=-1, random_state=42)
random_search.fit(X, y)


print("Best hyperparameters:", random_search.best_params_)
best_model = random_search.best_estimator_

# --- Evaluate on a Hold-out Test Set ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Test MSE: {mse:.2f}")
print(f"Test R²: {r2:.2f}")

# --- Generate Diagnostic Plots ---
target_names = ground_truth
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
for i, target in enumerate(target_names):
    ax = axes[i]
    ax.scatter(y_test[target], y_pred[:, i], alpha=0.7, edgecolors="k")
    ax.plot([y_test[target].min(), y_test[target].max()],
            [y_test[target].min(), y_test[target].max()],
            "r--", lw=2)
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title(f"{target}: Predicted vs. Actual")
plt.suptitle("Calibration Ensemble Pipeline Performance")
plot_path = os.path.join(ASSETS_DIR, "calibration_ensemble_pipeline_plots2.png")
plt.savefig(plot_path)
plt.close(fig)
print(f"Diagnostic plots saved to {plot_path}")

# --- Save the Trained Model as Pickle ---
pickle_path = os.path.join(SAVE_DIR, "calibration_ensemble_model.pkl")
with open(pickle_path, "wb") as f:
    pickle.dump(best_model, f)
print(f"Trained ensemble model saved to {pickle_path}")


# Specify one input per feature column.
initial_type = [(name, FloatTensorType([None, 1])) for name in computed_features]
onnx_model = convert_sklearn(best_model, initial_types=initial_type)
onnx_path = os.path.join(SAVE_DIR, "calibration_ensemble_model.onnx")
with open(onnx_path, "wb") as f:
    f.write(onnx_model.SerializeToString())
print(f"ONNX ensemble model saved to {onnx_path}")