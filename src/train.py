import os
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler  # Optional: scaling improves KNN performance

# Import your preprocessing function
from src.feature_engineering import load_dataset


def train_model(test_size=0.2, random_state=42, n_neighbors=3, model_dir="models", model_name="face_model.pkl"):
    """
    Loads dataset, splits, trains a KNN classifier, and saves the model.

    Args:
        test_size (float): Fraction of data to use as test set.
        random_state (int): Random seed for reproducibility.
        n_neighbors (int): Number of neighbors for KNN.
        model_dir (str): Directory to save the trained model.
        model_name (str): Name of the pickle file for the model.

    Returns:
        model: Trained KNeighborsClassifier.
        X_test: Test features.
        y_test: Test labels.
    """
    print("📦 Loading dataset...")
    X, y = load_dataset()

    print(f"Dataset size: {len(X)} samples")

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Optional: scale features for KNN (helps improve distance calculations)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train KNN model
    print(f"🤖 Training KNN model with {n_neighbors} neighbors...")
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)

    # Save model + scaler
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, model_name)
    with open(model_path, "wb") as f:
        pickle.dump({"model": model, "scaler": scaler}, f)  # Save scaler too!

    print(f"✅ Model trained and saved at '{model_path}'")

    return model, X_test, y_test


if __name__ == "__main__":
    train_model()