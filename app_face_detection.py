import streamlit as st
import cv2 
from PIL import Image, ImageEnhance
import numpy as np
import os
import time

@st.cache
def load_image(img):
    return Image.open(img)


def main():
    """Face Detection App"""

    st.title("Face Detection in the Browser")
    st.text('Built with `Streamlit` and `OpenCV`')

    activities = ['Detection', 'About']
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == 'Detection':
        st.subheader("Face Detection")
        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
        
        if image_file:
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
            st.text('File uploaded.')

            our_image = Image.open(image_file)
            st.text("Original Image")
            st.image(our_image)


        enhance_type = st.sidebar.radio("Enhance Type", ["Original", "Gray-Scale", "Contrast", "Brightness"])
        if enhance_type == 'Gray-Scale':
            new_img = np.array(our_image.convert(('RGB')))
            bw = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
            st.image(bw)
        if enhance_type == 'Contrast':
            c_rate = st.slider("Contrast", 0.5, 3.5)
            enhancer = ImageEnhance.Contrast(our_image)
            img_output = enhancer.enhance(c_rate)
            st.image(img_output)


    elif choice == 'About':
        st.subheader('About')


if __name__ == '__main__':
    main()
