from PIL import Image
import streamlit as st
from pathlib import Path

# Load Assets
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
img_Cert_1 = Image.open("images/Solidworks/Ex 223.PNG")
img_Cert_2 = Image.open("images/Solidworks/SW Mill Tut.PNG")
img_Cert_3 = Image.open("images/Solidworks/SW Weld Tut.PNG")
img_Cert_4 = Image.open("images/Solidworks/SW SM Tut.PNG")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("Solidworks Practice 4")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_4)
with text_column:
    st.subheader("Solidworks Sheet Metal Model")
    st.write(
        """
         Solidworks practice from Solidworks Tutorial
        """
        )
    st.markdown("[Learn from built-in Solidworks Tutorial]")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 3")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_3)
with text_column:
    st.subheader("Solidworks Weldment Model")
    st.write(
        """
         Solidworks practice from Solidworks Tutorial
        """
        )
    st.markdown("[Learn from built-in Solidworks Tutorial]")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 2")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_2)
with text_column:
    st.subheader("Solidworks Mill Model")
    st.write(
        """
         Solidworks practice from Solidworks Tutorial
        """
        )
    st.markdown("[Learn from built-in Solidworks Tutorial]")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 1")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("Solidworks 3D model")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=fFZTvQjRnyY)")