import joblib
from sklearn.ensemble import RandomForestClassifier
from preprocess import load_data

print("Loading training dataset...")

X_train, y_train = load_data("../dataset/train_dataset.csv")

print("Training model...")

model = RandomForestClassifier(
    n_estimators=150,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model,"../models/cyber_model.pkl")

print("Model trained and saved!")
