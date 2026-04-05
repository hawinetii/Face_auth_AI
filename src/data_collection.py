import cv2
import os

username = input("Enter your name: ")

folder_path = f"data/raw/{username}"
os.makedirs(folder_path, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        img_name = f"{folder_path}/{count}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Saved {img_name}")
        count += 1

        if count == 10:
            print("Collected 10 images")
            break

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()