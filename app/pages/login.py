import streamlit as st
import cv2
from config import DATA_PATH

def login_page():
    st.title("Login")

    # Optional: user enters name
    name = st.text_input("Enter your name (optional)")

    if st.button("Scan Face"):
        st.write("Starting face scan...")

        # Open webcam
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture image")
            return

        st.image(frame, channels="BGR")  # Show captured image
        cap.release()

        # Placeholder logic simulating a login
        if name:
            st.success(f"Login successful! Welcome {name}")
        else:
            st.warning("Face scanned (no name entered). Model integration will come later.")

        st.info("🔹 Note: ML model integration will be done later by teammates.")

        """
        result = model.predict(frame)
if result["match"]:
    st.success(f"Login successful! Welcome {result['name']}")
else:
    st.error("Face not recognized")
        """