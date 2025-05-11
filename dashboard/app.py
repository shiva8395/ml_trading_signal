import streamlit as st
import pandas as pd
import joblib
import yaml
from PIL import Image
with open(r"C:\Users\HP\Desktop\ml_trading_signal\config\strategy_config.yaml","r") as f:
    config=yaml.safe_load(f)
df = pd.read_csv(config["data_path"])
model = joblib.load(config["model_path"])

X=df[config["features"]]
preds=model.predict(X)
df['Predicted Signal'] = preds
st.title("ML Trading Signal Dashboard")
df['Close']=df['SMA_10']+(df['Returns']*2)
st.line_chart(df[['Close']])
st.bar_chart(df['Predicted Signal'])
st.subheader("🔍 Feature Importance (SHAP)")
shap_img = Image.open(r"C:\Users\HP\Desktop\ml_trading_signal\visuals\shap_summary.png")
st.image(shap_img, use_column_width=True)