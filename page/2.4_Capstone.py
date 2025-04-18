from PIL import Image
import streamlit as st
from pathlib import Path

# Load Assets
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
img_Cert_1 = Image.open("images/Capstone/Exploded.PNG")
img_Cert_2 = Image.open("images/Capstone/Front n Rear.PNG")
img_Cert_3 = Image.open("images/Capstone/Iso View.PNG")
img_Cert_4 = Image.open("images/Capstone/Side View.PNG")
img_Cert_5 = Image.open("images/Capstone/Top View.PNG")
img_Cert_6 = Image.open("images/Capstone/WAS.png")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("3D Model of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((2,2))
    
with image_column:
    st.image(img_Cert_6)
with text_column:
    st.subheader("3D Model using Blender")
   
with st.container():
    st.write("---")
    st.header("AutoCAD of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((2,2))
    
with image_column:
    st.image(img_Cert_5)
with text_column:
    st.subheader("Top View of Capstone Project")
    
with st.container():
    st.write("---")
    st.header("AutoCAD of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((2,2))
    
with image_column:
    st.image(img_Cert_4)
with text_column:
    st.subheader("Side View of Capstone Project")
    
with st.container():
    st.write("---")
    st.header("AutoCAD of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((2,2))
    
with image_column:
    st.image(img_Cert_3)
with text_column:
    st.subheader("Isometric View of Capstone Project")
    
with st.container():
    st.write("---")
    st.header("AutoCAD of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((2,2))
    
with image_column:
    st.image(img_Cert_2)
with text_column:
    st.subheader("Front and Rear View of Capstone Project")
    
with st.container():
    st.write("---")
    st.header("AutoCAD of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((2,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("Exploded View of Capstone Project")

