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
