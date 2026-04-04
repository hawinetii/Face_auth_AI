# src/evaluate.py

import pickle
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from src.feature_engineering import create_dataset   # assume this returns X, y

def evaluate():
    # 1. Load dataset
    X, y = create_dataset()   # returns flattened images and labels

    # 2. Split (same as in train.py: 80% train, 20% test, random_state=42)
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Load trained model
    with open('models/face_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # 4. Predict
    y_pred = model.predict(X_test)

    # 5. Metrics
    acc = accuracy_score(y_test, y_pred)
    print(f"Test Accuracy: {acc * 100:.2f}%")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

   
    distances, _ = model.kneighbors(X_test)
    print(f"\nAverage distance to nearest neighbor: {np.mean(distances):.3f}")

if __name__ == "__main__":
    evaluate()
