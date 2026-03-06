from flask import Flask, request, jsonify
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

model = joblib.load("../models/cyber_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    df = pd.DataFrame(data)

    encoder = LabelEncoder()

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = encoder.fit_transform(df[col])

    prediction = model.predict(df)

    return jsonify({"prediction": prediction.tolist()})


if __name__ == "__main__":
    app.run(port=5000)
