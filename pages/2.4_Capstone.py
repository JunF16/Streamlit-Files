from PIL import Image
import streamlit as st

# Load Assets
img_Cert_1 = Image.open(r"images/Capstone/Exploded.png")
img_Cert_2 = Image.open(r"images/Capstone/Front n Rear.png")
img_Cert_3 = Image.open(r"images/Capstone/Iso View.png")
img_Cert_4 = Image.open(r"images/Capstone/Side View.png")
img_Cert_5 = Image.open(r"images/Capstone/Top View.png")
img_Cert_6 = Image.open(r"images/Capstone/WAS.png")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("3D Model of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_6)
with text_column:
    st.subheader("3D Model of Capstone Project")
   
with st.container():
    st.write("---")
    st.header("AutoCAD of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_5)
with text_column:
    st.subheader("Top View of Capstone Project")
    
with st.container():
    st.write("---")
    st.header("AutoCAD of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_4)
with text_column:
    st.subheader("Side View of Capstone Project")
    
with st.container():
    st.write("---")
    st.header("AutoCAD of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_3)
with text_column:
    st.subheader("Isometric View of Capstone Project")
    
with st.container():
    st.write("---")
    st.header("AutoCAD of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_2)
with text_column:
    st.subheader("Front and Rear View of Capstone Project")
    
with st.container():
    st.write("---")
    st.header("AutoCAD of Capstone Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("Exploded View of Capstone Project")

