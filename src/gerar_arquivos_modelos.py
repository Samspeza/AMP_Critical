import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Recriação dos dados
np.random.seed(42)
X = np.random.uniform(0, 10, size=(1000, 2))
y = 5 * X[:, 0] + np.sin(X[:, 1]) * 10 + np.random.normal(0, 2, size=1000)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Treinamento
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predição e cálculo do threshold
y_pred = model.predict(X_test)
erros = abs(y_test - y_pred)
threshold = np.percentile(erros, 90)

# Exportação
joblib.dump(model, "random_forest_model.joblib")
joblib.dump(threshold, "threshold_erro.joblib")

print("Modelo e threshold salvos com sucesso.")