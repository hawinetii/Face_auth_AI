import cv2
import os

def data_collection(name, DATA_PATH, num_images=5):
    """
    Captures images from webcam for a given user and saves them to DATA_PATH/<name>/.

    Args:
        name (str): User name
        DATA_PATH (str): Folder where data is stored
        num_images (int): Number of images to capture
    """
    # Create folder for the user
    user_folder = os.path.join(DATA_PATH, name)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    cap = cv2.VideoCapture(0)
    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # Save image
        img_path = os.path.join(user_folder, f"{name}_{count+1}.jpg")
        cv2.imwrite(img_path, frame)
        count += 1

    cap.release()
    return f"{count} images saved for {name}"