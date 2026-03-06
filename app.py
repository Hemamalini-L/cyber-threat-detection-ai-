import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

st.title("Cyber Threat Detection System")

model = joblib.load("models/cyber_model.pkl")

uploaded_file = st.file_uploader("Upload Network Traffic CSV")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # Encode categorical columns
    encoder = LabelEncoder()

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = encoder.fit_transform(df[col])

    predictions = model.predict(df)

    df["Prediction"] = predictions

    st.write("Detection Results")
    st.dataframe(df)

    st.bar_chart(df["Prediction"].value_counts())
