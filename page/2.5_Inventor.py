from PIL import Image
import streamlit as st
from pathlib import Path

# Load Assets (for vids: change video_bytes&st.video numbering)
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
img_Cert_1 = Image.open("images/Inventor/MAHTABALAM 1.PNG")
img_Cert_2 = Image.open("images/Inventor/MAHTABALAM 2.PNG")
video_file_1 = open("videos/Fidget Spinner.mp4","rb")
img_Cert_3 = Image.open("images/Inventor/MAHTABALAM 3.PNG")
img_Cert_4 = Image.open("images/Inventor/MAHTABALAM 4.PNG")
video_file_2 = open("videos/QRM.mp4","rb") 
video_file_3 = open("videos/Ball Bearing.mp4","rb")
video_file_4 = open("videos/Arbor Press.mp4", "rb")

# Projects (add above succeeding projects)
with st.container():
    st.write("---")
    st.header("Autodesk Inventor practice 8")
    st.write("##")
    video_column, text_column = st.columns((1,2))
    
with video_column:
    video_bytes = video_file_4.read()
    st.video(video_file_4)
with text_column:
    st.subheader("Arbor Press")
    st.write(
        """
         Inventor Practice from 3D Parametric Solid Model Drawing
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=H9XeTY5CNQw)")

with st.container():
    st.write("---")
    st.header("Autodesk Inventor practice 7")
    st.write("##")
    video_column, text_column = st.columns((1,2))
    
with video_column:
    video_bytes = video_file_3.read()
    st.video(video_file_3)
with text_column:
    st.subheader("Ball Bearing")
    st.write(
        """
         Inventor Practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/playlist?list=PLRhna5_X7uWvjFID3uU0vKxpiuw8XvF35)")

with st.container():
    st.write("---")
    st.header("Autodesk Inventor practice 6")
    st.write("##")
    video_column, text_column = st.columns((1,2))
    
with video_column:
    video_bytes = video_file_2.read()
    st.video(video_file_2)
with text_column:
    st.subheader("Quick Return Mechanism")
    st.write(
        """
         Inventor Practice from CADemist
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/@cademist)")

with st.container():
    st.write("---")
    st.header("Autodesk Inventor practice 5")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_4)
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
    st.header("Autodesk Inventor practice 4")
    st.write("##")
    video_column, text_column = st.columns((1,2))
    
with video_column:
    video_bytes = video_file_1.read()
    st.video(video_file_1)
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
    st.header("Autodesk Inventor practice 3")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_3)
with text_column:
    st.subheader("Inventor 3D object")
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