import os
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Import your preprocessing function
from src.feature_engineering import load_dataset

def train_model():
    print("📦 Loading dataset...")
    X, y = load_dataset()

    print(f"Dataset size: {len(X)} samples")

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train KNN model
    print("🤖 Training model...")
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    # Save model
    os.makedirs("models", exist_ok=True)
    with open("models/face_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("✅ Model trained and saved!")

    return model, X_test, y_test


if __name__ == "__main__":
    train_model()