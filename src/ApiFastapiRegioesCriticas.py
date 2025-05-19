from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI()

model = joblib.load("random_forest_model.joblib")
threshold = joblib.load("threshold_erro.joblib")

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.post("/verificar_regiao_critica")
def verificar_regiao(dados: InputData):
    X = pd.DataFrame([[dados.feature1, dados.feature2]], columns=["feature1", "feature2"])
    pred = model.predict(X)[0]

    erro_estimado = abs(pred - (5*dados.feature1 + np.sin(dados.feature2)*10))
    is_critico = erro_estimado >= threshold

    return {
        "previsao": pred,
        "erro_estimado": erro_estimado,
        "regiao_critica": is_critico
    }