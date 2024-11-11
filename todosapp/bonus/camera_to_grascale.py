import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    camera_img = st.camera_input("Camera")
    if camera_img:
        img = Image.open(camera_img)
        grey_img = img.convert("L")
        st.image(grey_img)