import pandas as pd

def preprocess_data(file):

    df = pd.read_csv(file)

    # Drop label if exists
    if "label" in df.columns:
        df = df.drop("label", axis=1)

    # Fill missing
    df = df.fillna(0)

    return df
