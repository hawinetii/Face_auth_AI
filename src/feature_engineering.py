import os
import cv2
import numpy as np

def load_dataset():
    data_path = "data/raw"
    X, y = [], []

    if not os.path.exists(data_path):
        return np.array([]), np.array([])

    for user in os.listdir(data_path):
        user_path = os.path.join(data_path, user)

        if not os.path.isdir(user_path):
            continue

        for img_name in os.listdir(user_path):
            img_path = os.path.join(user_path, img_name)

            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                continue

            img = cv2.resize(img, (64, 64))
            img = img / 255.0

            X.append(img.flatten())
            y.append(user)

    return np.array(X), np.array(y)
import numpy as np
from preprocessing import preprocess_images

def create_dataset():

    # Get processed images
    faces, labels, label_map = preprocess_images()

    # Normalize pixel values
    faces = faces / 255.0

    # Reshape for ML models
    faces = faces.reshape(
        faces.shape[0],
        100,
        100,
        1
    )

    return faces, labels, label_map


if __name__ == "__main__":

    X, y, label_map = create_dataset()

    print("Dataset Created")
    print("Number of samples:", len(X))
    print("Labels:", label_map)
