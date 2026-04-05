import cv2
import os
import numpy as np

# Load face detector
face_cascade = cv2.CascadeClassifier(
    "src/haarcascade_frontalface_default.xml"
)

def preprocess_images(data_path="data/raw"):
    
    faces = []
    labels = []

    label_map = {}
    label_id = 0

    # Loop through each user folder
    for person_name in os.listdir(data_path):

        person_folder = os.path.join(data_path, person_name)

        if not os.path.isdir(person_folder):
            continue

        # Assign label number
        label_map[label_id] = person_name

        for image_name in os.listdir(person_folder):

            image_path = os.path.join(person_folder, image_name)

            # Read image
            img = cv2.imread(image_path)

            if img is None:
                continue

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect face
            faces_detected = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5
            )

            # Crop face
            for (x, y, w, h) in faces_detected:

                face = gray[y:y+h, x:x+w]

                # Resize face
                face = cv2.resize(face, (100, 100))

                faces.append(face)
                labels.append(label_id)

        label_id += 1

    return np.array(faces), np.array(labels), label_map
