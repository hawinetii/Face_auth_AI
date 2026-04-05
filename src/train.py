import os
import pickle
import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

DATA_PATH = "data"
MODEL_PATH = "models/face_model.pkl"

os.makedirs("models", exist_ok=True)

def load_dataset():
    X = []
    y = []

    face_cascade = cv2.CascadeClassifier("src/haarcascade_frontalface_default.xml")

    for person in os.listdir(DATA_PATH):
        person_path = os.path.join(DATA_PATH, person)

        if not os.path.isdir(person_path):
            continue

        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)

            img = cv2.imread(img_path)
            if img is None:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) == 0:
                continue

            x, y_, w, h = faces[0]
            face = gray[y_:y_+h, x:x+w]

            face = cv2.resize(face, (100, 100)).flatten()

            X.append(face)
            y.append(person)

    return np.array(X), np.array(y)


def train_model():
    print("📦 Loading dataset...")
    X, y = load_dataset()

    if len(X) == 0:
        raise ValueError("❌ No faces found in dataset.")

    print(f"Dataset size: {len(X)} samples")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("🤖 Training model...")
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"📊 Accuracy: {acc * 100:.2f}%")

    with open(MODEL_PATH, "wb") as f:
        pickle.dump({"model": model, "scaler": scaler}, f)

    print("✅ Model saved!")

    return model


if __name__ == "__main__":
    train_model()