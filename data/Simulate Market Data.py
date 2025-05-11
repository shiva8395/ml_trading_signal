import pandas as pd
import numpy as np
np.random.seed(42)
n=200
data =pd.DataFrame({
    'SMA_10': np.random.rand(n) * 100,
    'SMA_50': np.random.rand(n) * 100,
    'Volatility': np.random.rand(n) * 10,
    'Returns': np.random.randn(n),
    'RSI': np.random.rand(n) * 100,
    'Signal': np.random.randint(0, 2, size=n)
})
data.to_csv(r"C:\Users\HP\Desktop\ml_trading_signal\data\market_data.csv", index=False)
print("✅ market_data.csv saved.")