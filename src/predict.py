import pickle
import cv2

model = pickle.load(open("models/face_model.pkl", "rb"))

def predict(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cv2.resize(gray, (64, 64))
    face = face.flatten().reshape(1, -1)

    pred = model.predict(face)[0]

    dist, _ = model.kneighbors(face)

    if dist[0][0] > 0.6:
        return "Denied"
    return f"Granted: {pred}"