from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd
df = pd.read_csv(r"C:\Users\HP\Desktop\ml_trading_signal\data\market_data.csv")
X = df[['SMA_10', 'SMA_50', 'Volatility', 'Returns', 'RSI']]
y = df['Signal']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)
joblib.dump(model, r"C:\Users\HP\Desktop\ml_trading_signal\models\rf_model.pkl")