import os
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from src.feature_engineering import load_dataset


def train_model():
    print("📦 Loading dataset...")
    X, y = load_dataset()

    if len(X) == 0:
        raise ValueError("❌ Dataset is empty. Add images to data/raw/")

    print(f"Dataset size: {len(X)} samples")

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train
    print("🤖 Training model...")
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"📊 Accuracy: {acc * 100:.2f}%")

    # Save
    os.makedirs("models", exist_ok=True)
    with open("models/face_model.pkl", "wb") as f:
        pickle.dump({"model": model, "scaler": scaler}, f)

    print("✅ Model saved!")

    return model


if __name__ == "__main__":
    train_model()