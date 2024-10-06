from PIL import Image
import streamlit as st

# Load Assets
img_Cert_1 = Image.open(r"images/Inventor/MAHTABALAM 1.png")

# Projects
with st.container():
    st.write("---")
    st.header("Autodesk Inventor practice 1")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("Inventor 3D object")
    st.write(
        """
         Inventor practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/playlist?list=PLRhna5_X7uWvjFID3uU0vKxpiuw8XvF35)")