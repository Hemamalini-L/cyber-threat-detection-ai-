import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(path):

    df = pd.read_csv(path)

    # Encode categorical columns
    categorical = ["protocol_type","service","flag"]

    encoder = LabelEncoder()

    for col in categorical:
        if col in df.columns:
            df[col] = encoder.fit_transform(df[col])

    # Split features and label
    X = df.drop("label", axis=1)
    y = df["label"]

    return X, y
