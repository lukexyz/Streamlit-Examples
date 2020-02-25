import streamlit as st
import cv2 
from PIL import Image, ImageEnhance
import numpy as numpy
import os
import time



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


    elif choice == 'About':
        st.subheader('About')


if __name__ == '__main__':
    main()
