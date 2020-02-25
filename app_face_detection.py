import streamlit as st
import cv2 
from PIL import Image, ImageEnhance
import numpy as np
import os
import time

@st.cache
def load_image(image_file):
    # img = Image.open(image_file)
    # img_out = cv2.resize(img, None, fx=0.25, fy=0.25)
    return Image.open(image_file)

face_cascade = cv2.CascadeClassifier('data/cascades/haarcascade_frontalface_alt.xml')

@st.cache
def detect_faces(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    bw = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Detect Face
    faces = face_cascade.detectMultiScale(bw, 1.1, 4)
    # Draw Rectangle
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    return img, faces

def main():
    """Face Detection App"""
    loader = True
    st.title("Face Detection in the Browser")
    st.text('Built with `Streamlit` and `OpenCV`')

    activities = ['Detection', 'About']
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == 'Detection':
        st.subheader("Face Detection")
        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
        
        if image_file:
            st.text('File uploaded.')
            our_image = Image.open(image_file)
            st.text("Original Image")
            st.image(our_image)
            


        enhance_type = st.sidebar.radio("Enhance Type", 
                       ["Original", "Gray-Scale", "Contrast", "Brightness", "Blurring"])
        
        if enhance_type == 'Gray-Scale':
            new_img = np.array(our_image.convert(('RGB')))
            bw = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
            st.image(bw)
        if enhance_type == 'Contrast':
            c_rate = st.slider("Contrast", 0.5, 3.5)
            enhancer = ImageEnhance.Contrast(our_image)
            img_output = enhancer.enhance(c_rate)
            st.image(img_output)
        if enhance_type == 'Brightness':
            c_rate = st.slider("Brightness", 0.5, 3.5)
            enhancer = ImageEnhance.Brightness(our_image)
            img_output = enhancer.enhance(c_rate)
            st.image(img_output)
        if enhance_type == 'Blurring':
            b_rate = st.slider("Blurring Rate", 0.5, 3.5)
            new_img = np.array(our_image.convert(('RGB')))
            img = cv2.cvtColor(new_img,1)
            blur_img = cv2.GaussianBlur(img,(11,11), b_rate)
            st.image(blur_img)

        # Face Detection
        task = ['None', 'Faces', 'Smiles', 'Eyes', 'Cannize']
        feature_choice = st.sidebar.selectbox("Find Features", task)
        if st.button('Find Features'):

            if feature_choice == 'Faces':
                result_img, result_faces = detect_faces(our_image)
                st.image(result_img)



    elif choice == 'About':
        st.subheader('About')


if __name__ == '__main__':
    main()
