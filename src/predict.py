import pickle
import cv2
import numpy as np

# Load model and scaler
with open("models/face_model.pkl", "rb") as f:
    data = pickle.load(f)
    model = data["model"]
    scaler = data["scaler"]

def predict(frame, distance_threshold=0.6):
    """
    Predicts the identity from a given frame.

    Args:
        frame: BGR image from webcam or video.
        distance_threshold: Max KNN distance to accept a match.

    Returns:
        str: "Granted: <label>" if matched, else "Denied"
    """
    # Convert to grayscale and resize
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cv2.resize(gray, (64, 64))

    # Flatten and scale
    face_flat = face.flatten().reshape(1, -1)
    face_scaled = scaler.transform(face_flat)

    # Predict label
    pred = model.predict(face_scaled)[0]

    # Check nearest neighbor distance
    dist, _ = model.kneighbors(face_scaled)

    if dist[0][0] > distance_threshold:
        return "Denied"
    return f"Granted: {pred}"