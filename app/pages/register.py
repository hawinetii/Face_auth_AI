import streamlit as st
import os
from PIL import Image
from config import DATA_PATH  # Ensure DATA_PATH = "data"

MAX_IMAGES = 5  # Maximum images per user

def register_page():
    st.title("Multi-User Face Registration")
    st.write(f"Each user can take up to {MAX_IMAGES} images.")

    # Initialize session state
    if "current_user" not in st.session_state:
        st.session_state.current_user = ""
    if "img_count" not in st.session_state:
        st.session_state.img_count = 0
    if "camera_key" not in st.session_state:
        st.session_state.camera_key = 0  # forces camera reset

    # Input user name
    name = st.text_input("Enter user name", value=st.session_state.current_user)

    # If the user changes the name, reset their image count
    if name != st.session_state.current_user:
        st.session_state.current_user = name
        st.session_state.img_count = 0
        st.session_state.camera_key += 1  # reset camera for new user

    if not name.strip():
        st.warning("Please enter a user name to start registration.")
        return

    # Prevent taking more than MAX_IMAGES
    if st.session_state.img_count >= MAX_IMAGES:
        st.success(f"{name} registration complete! {MAX_IMAGES} images saved.")
        st.info("Enter the next user name to start a new registration.")
        return

    # Camera input with dynamic key
    img_file = st.camera_input("Take a picture", key=st.session_state.camera_key)

    if img_file is not None:
        image = Image.open(img_file)
        st.image(image, caption=f"Preview ({st.session_state.img_count + 1}/{MAX_IMAGES})", width=400)

        if st.button("Save Image"):
            # Create folder for this user
            user_path = os.path.join(DATA_PATH, name)
            os.makedirs(user_path, exist_ok=True)

            # Save image
            filename = f"{st.session_state.img_count}.png"
            file_path = os.path.join(user_path, filename)
            image.save(file_path)

            st.session_state.img_count += 1
            st.success(f"Saved image {st.session_state.img_count} for {name} successfully!")

            # Reset camera for next image
            st.session_state.camera_key += 1

