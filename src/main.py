import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
import shap

np.random.seed(42)
X = np.random.uniform(0, 10, size=(1000, 2))
y = 5 * X[:, 0] + np.sin(X[:, 1]) * 10 + np.random.normal(0, 2, size=1000)
df = pd.DataFrame(X, columns=["feature1", "feature2"])
df["target"] = y

X_train, X_test, y_train, y_test = train_test_split(df[["feature1", "feature2"]], df["target"], test_size=0.2)

# --- Treinamento dos Modelos ---
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
y_pred_lr = model_lr.predict(X_test)

model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)
y_pred_rf = model_rf.predict(X_test)

# --- Avaliação ---
def avaliar(y_true, y_pred, nome_modelo):
    print(f"\nModelo: {nome_modelo}")
    print("RMSE:", np.sqrt(mean_squared_error(y_true, y_pred)))
    print("R�:", r2_score(y_true, y_pred))

avaliar(y_test, y_pred_lr, "Regress�o Linear")
avaliar(y_test, y_pred_rf, "Random Forest")

# --- Identificação de Regiões Críticas ---
residuals = y_test - y_pred_rf
critical_points = X_test.copy()
critical_points["residual"] = residuals

# Definindo regiões críticas como top 10% maiores erros absolutos
threshold = np.percentile(abs(residuals), 90)
critical_points["is_critical"] = abs(residuals) >= threshold

# --- Visualização das Regioes Criticas ---
plt.figure(figsize=(10,6))
sns.scatterplot(data=critical_points, x="feature1", y="feature2", hue="is_critical", palette={True: 'red', False: 'blue'})
plt.title("Regi�es Cr�ticas com base no erro do modelo Random Forest")
plt.xlabel("feature1")
plt.ylabel("feature2")
plt.show()

explainer = shap.Explainer(model_rf, X_test)
shap_values = explainer(X_test)
shap.summary_plot(shap_values, X_test)
