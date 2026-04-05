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