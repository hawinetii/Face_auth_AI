import cv2
import pickle
import numpy as np
import os

MODEL_PATH = "models/face_model.pkl"

def predict_face(image_input):
    try:
        # Load model
        if not os.path.exists(MODEL_PATH):
            return "Error: Model not found. Train first."

        with open(MODEL_PATH, "rb") as f:
            data = pickle.load(f)

        model = data["model"]
        scaler = data["scaler"]

        # ---------------- HANDLE IMAGE ----------------
        # 🔥 ONLY load with imread IF it's a string path
        if isinstance(image_input, str):
            img = cv2.imread(image_input)
        else:
            img = image_input  # already an image (numpy array)

        # Safety check
        if img is None:
            return "Error: Invalid image input"

        # Convert to grayscale
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Resize
        img = cv2.resize(img, (64, 64))

        # Flatten + scale
        img = img.flatten().reshape(1, -1)
        img = scaler.transform(img)

        # Predict
        prediction = model.predict(img)

        return prediction[0]

    except Exception as e:
        return f"Error: {str(e)}"
    print(type(image_input))