import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Loading Dataset...")

df = pd.read_csv("data/train_dataset.csv")

X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier()

model.fit(X, y)

joblib.dump(model, "model/cyber_model.pkl")

print("Model Saved")
