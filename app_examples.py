import streamlit as st
import time
import matplotlib.pyplot as plt

# Titles
st.title("Streamlit Examples")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is regular text.")
st.markdown("#### This is `Markdown`")

# Misc text
st.success("Successful")
st.info("Information")
st.warning("This is a warning!")
st.error("This is an error -- Danger")
st.exception("NameError()")


st.help(range)
st.write("Text with write")
st.write(range(10))


# Images
from PIL import Image
img = Image.open("img/logo.jpg")
st.image(img, caption='Streamlit', width=150)


# Widgets
if st.checkbox("Show/Hide"):
    st.text("Showing Tickbox")


# Radio
status = st.radio("Radio button:", ("Active", "Inactive"))
if status == 'Active':
    st.success("You are Active")
else:
    st.warning("Inactive")

# SelectBox
occupation = st.selectbox("Your Occupation", ['Data Scientist', 'Machine Learning Engineer'])
st.write("You selected: ", occupation)

years = st.selectbox("Years Experience", list(range(10)))
st.write("You selected: ", years)

# MultiSelect
location = st.multiselect("Pick a Location", ("London, UK", "Wellington, New Zealand", "Accra, Ghana"))
if location: st.write("You selected: ", location)


# Timers and Spinners
if st.checkbox("Activate Timer"):
    with st.spinner('Progress bar starting in 2 seconds...'):
        time.sleep(2)
        st.success('Done!')
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1)


# Buttons
st.button("Simple Button")
if st.button("About"):
    st.text("You clicked the button. Well done!")


# Text Input
title = st.text_input('Enter Your Name', 'Type Name Here...')
if st.button("Submit"): 
    st.write('Your name is', title)


# Slider
level = st.slider("What is your level", 1, 5)
if level: st.write(f"You're at level {level}, Nice!")

# Functions
# @st.cache
def run_fn(s):
    return f"{s}"
st.write(run_fn(level))


# Plot
st.pyplot()

"""

> streamlit run app_examples.py

"""