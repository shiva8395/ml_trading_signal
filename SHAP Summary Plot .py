import shap
import pandas as pd
import joblib
import matplotlib.pyplot as plt
model=joblib.load(r"C:\Users\HP\Desktop\ml_trading_signal\models\rf_model.pkl")
X= pd.read_csv(r"C:\Users\HP\Desktop\ml_trading_signal\data\market_data.csv")[
    ['SMA_10', 'SMA_50', 'Volatility', 'Returns', 'RSI']
]
explainer= shap.TreeExplainer(model)
shap_values=explainer.shap_values(X)
shap.summary_plot(shap_values,X,plot_type= "bar", show=False)
plt.tight_layout()
plt.savefig(r"C:\Users\HP\Desktop\ml_trading_signal\visuals\shap_summary.png")
plt.show()
