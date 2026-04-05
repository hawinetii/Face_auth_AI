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
    Predict identity from webcam frame
    """

    # Safety check
    if frame is None:
        return "❌ No image captured"

    try:
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize
        face = cv2.resize(gray, (64, 64))

        # Flatten + scale
        face_flat = face.flatten().reshape(1, -1)
        face_scaled = scaler.transform(face_flat)

        # Predict
        pred = model.predict(face_scaled)[0]

        # Distance (confidence)
        dist, _ = model.kneighbors(face_scaled)
        confidence = dist[0][0]

        # Decision
        if confidence > distance_threshold:
            return "❌ Access Denied"
        else:
            return f"✅ Access Granted: {pred}"

    except Exception as e:
        return f"⚠️ Error: {str(e)}"