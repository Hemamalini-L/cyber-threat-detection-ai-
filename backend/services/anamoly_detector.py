import joblib
import pandas as pd

model = joblib.load("model/cyber_model.pkl")

def detect_anomaly(df):

    predictions = model.predict(df)

    return predictions
