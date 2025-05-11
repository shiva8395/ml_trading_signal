from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import yaml
with open(r"C:\Users\HP\Desktop\ml_trading_signal\config\strategy_config.yaml") as f:
 config=yaml.safe_load(f)
model= joblib.load(config["model_path"])
features= config["features"]
app= FastAPI(title="ML Trading Signal API", version="1.0")
class SignalRequest(BaseModel):
    SMA_10: float
    SMA_50: float
    Volatility: float
    Returns: float
    RSI: float
@app.get("/health")
def health_check():
    return {"status": "ok"}
@app.get("/features")
def get_features():
    return {"features": features}
@app.post("/predict")
def predict_signal(data: SignalRequest):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)[0]
    return {
        "prediction": int(prediction),
        "signal": "BUY" if prediction == 1 else "SELL"
    }