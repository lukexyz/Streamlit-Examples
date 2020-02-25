import streamlit as st
import cv2 
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np
import os
import time

@st.cache
def load_image(image_file):
    # img = Image.open(image_file)
    # img_out = cv2.resize(img, None, fx=0.25, fy=0.25)
    return Image.open(image_file)

face_cascade = cv2.CascadeClassifier('data/cascades/haarcascade_frontalface_alt.xml')
smile_cascade = cv2.CascadeClassifier('data/cascades/haarcascade_smile.xml')


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

@st.cache
def detect_smiles(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    bw = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Detect Smile
    smiles = smile_cascade.detectMultiScale(bw, 1.1, 4)
    # Draw Rectangle
    for (x,y,w,h) in smiles:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    return img, smiles

def main():
    """Face Detection App"""
    loader = True
    st.title("Face Detection in the Browser")
    st.text('Built with `Streamlit` and `OpenCV`')

    activities = ['Image Processing', 'About']
    choice = st.sidebar.selectbox("Select Activity", activities)


    if choice == 'Image Processing':
        st.subheader("Image Processing with Streamlit")
        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
        
        # Select Image
        if image_file:
            st.text('File uploaded.')
            our_image = Image.open(image_file)
            st.text("Original Image")
            st.image(our_image)

        # Processing Enhancments    
        enhance_type = st.sidebar.radio("Enhance Type", 
                       ["Original", "Gray-Scale", "Vignette", "Contrast", "Brightness", "Blurring"])
        
        if enhance_type == 'Gray-Scale':
            new_img = np.array(our_image.convert(('RGB')))
            bw = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
            st.image(bw)

        elif enhance_type == 'Contrast':
            c_rate = st.slider("Contrast", 0.5, 3.5)
            enhancer = ImageEnhance.Contrast(our_image)
            img_output = enhancer.enhance(c_rate)
            st.image(img_output)

        elif enhance_type == 'Brightness':
            c_rate = st.slider("Brightness", 0.5, 3.5)
            enhancer = ImageEnhance.Brightness(our_image)
            img_output = enhancer.enhance(c_rate)
            st.image(img_output)

        elif enhance_type == 'Blurring':
            b_rate = st.slider("Blurring Rate", 0.5, 3.5)
            new_img = np.array(our_image.convert(('RGB')))
            img = cv2.cvtColor(new_img,1)
            blur_img = cv2.GaussianBlur(img,(11,11), b_rate)
            st.image(blur_img)

        elif enhance_type == 'Vignette':
            v_rate = st.slider('Vignette Sigma', 0, 900)
            new_img = np.array(our_image.convert(('RGB')))
            rows, cols = new_img.shape[:2]
            zeros = np.copy(new_img)
            zeros[:,:,:] = 0
            a = cv2.getGaussianKernel(cols, v_rate)
            b = cv2.getGaussianKernel(rows, v_rate)
            c = b*a.T
            d = c/c.max()   
            zeros[:,:,0] = new_img[:,:,0]*d
            zeros[:,:,1] = new_img[:,:,1]*d
            zeros[:,:,2] = new_img[:,:,2]*d
            st.image(zeros)
            
        # Face Detection
        task = ['None', 'Faces', 'Smiles']
        feature_choice = st.sidebar.selectbox("Find Features", task)
        if st.button('Find Features'):

            if feature_choice == 'Faces':
                result_img, result_faces = detect_faces(our_image)
                st.image(result_img)
                st.success(f"Found `{len(result_faces)}` faces.")

            elif feature_choice == 'Smiles':
                result_img, result_smiles = detect_smiles(our_image)
                st.image(result_img)
                st.success(f"Found `{len(result_smiles)}` smiles.")



    elif choice == 'About':
        st.subheader('About')


if __name__ == '__main__':
    main()
