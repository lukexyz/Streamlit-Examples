import streamlit as st
import cv2 
from PIL import Image, ImageEnhance
import numpy as numpy
import os


def main():
    """Face Detection App"""

    st.title("Face Detection in the Browser")
    st.text('Built with `Streamlit` and `OpenCV`')

    activities = ['Detection', 'About']
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == 'Detection':
        st.subheader("Face Detection")
    elif choice == 'About':
        st.subheader('About')


if __name__ == '__main__':
    main()
