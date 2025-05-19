# treinamento_xgboost_mlp.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor
from sklearn.neural_network import MLPRegressor

# Gera��o dos dados simulados
np.random.seed(42)
X = np.random.uniform(0, 10, size=(1000, 2))
y = 5 * X[:, 0] + np.sin(X[:, 1]) * 10 + np.random.normal(0, 2, size=1000)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# --- XGBoost ---
model_xgb = XGBRegressor(n_estimators=100)
model_xgb.fit(X_train, y_train)
y_pred_xgb = model_xgb.predict(X_test)

print("XGBoost")
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_xgb)))
print("R:", r2_score(y_test, y_pred_xgb))

# --- MLP ---
model_mlp = MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=1000)
model_mlp.fit(X_train, y_train)
y_pred_mlp = model_mlp.predict(X_test)

print("\nMLP Regressor")
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_mlp)))
print("R:", r2_score(y_test, y_pred_mlp))