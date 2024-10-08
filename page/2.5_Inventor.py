from PIL import Image
import streamlit as st
from pathlib import Path

# Load Assets
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
img_Cert_1 = Image.open("images/Inventor/MAHTABALAM 1.PNG")
img_Cert_2 = Image.open("images/Inventor/MAHTABALAM 2.PNG")
video_file = open("videos/Fidget Spinner.mp4","rb")

# Projects (add above succeeding projects)
with st.container():
    st.write("---")
    st.header("Autodesk Inventor practice 3")
    st.write("##")
    video_column, text_column = st.columns((1,2))
    
with video_column:
    video_bytes = video_file.read()
    st.video(video_file)
with text_column:
    st.subheader("Fidget Spinner")
    st.write(
        """
         Inventor Practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/playlist?list=PLRhna5_X7uWvjFID3uU0vKxpiuw8XvF35)")

with st.container():
    st.write("---")
    st.header("Autodesk Inventor practice 2")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_2)
with text_column:
    st.subheader("Inventor 3D object")
    st.write(
        """
         Inventor practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/playlist?list=PLRhna5_X7uWvjFID3uU0vKxpiuw8XvF35)")

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