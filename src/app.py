import streamlit as st
import pandas as pd
import joblib
from src.threat_engine import threat_level

st.set_page_config(layout="wide")

st.title("🛡 Cyber Threat Detection System")

model = joblib.load("models/cyber_model.pkl")

uploaded_file = st.file_uploader("Upload Network Traffic CSV")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    predictions = model.predict(df)

    df["prediction"] = predictions

    df["severity"] = df["prediction"].apply(threat_level)

    st.subheader("Detection Results")

    st.dataframe(df)

    st.subheader("Threat Distribution")

    st.bar_chart(df["severity"].value_counts())
