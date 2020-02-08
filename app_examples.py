import streamlit as st

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




"""

> streamlit run app.py

"""