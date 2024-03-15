import streamlit as st 
from PIL import Image

image = Image.open(path)

st.image(image)
