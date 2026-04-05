import os
import cv2
import pickle
import numpy as np
from src.preprocessing import preprocess_image   # provided by Mekdes

def test_full_pipeline():
    # Path to one test image (choose any existing user)
    # Adjust the username and image index as needed
    test_image_path = "data/raw/Mekdes/0.jpg"
    expected_user = "Mekdes"

    # 1. Preprocess
    processed_img = preprocess_image(test_image_path)
    assert processed_img is not None, "❌ No face detected in test image"

    # 2. Flatten to 1D feature vector
    features = processed_img.flatten().reshape(1, -1)

    # 3. Load model
    with open('models/face_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # 4. Predict
    predicted_label = model.predict(features)[0]

    # 5. Assert
    assert predicted_label == expected_user, f"Expected {expected_user}, got {predicted_label}"
    print("✅ Pipeline test passed: prediction matches expected user.")

if __name__ == "__main__":
    test_full_pipeline()

