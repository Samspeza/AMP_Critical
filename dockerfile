# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    scikit-learn \
    pandas \
    numpy \
    xgboost \
    joblib \
    matplotlib \
    seaborn \
    shap

EXPOSE 8000

CMD ["uvicorn", "api_fastapi_regioes_criticas:app", "--host", "0.0.0.0", "--port", "8000"]