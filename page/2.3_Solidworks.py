from PIL import Image
import streamlit as st
from pathlib import Path

# Load Assets
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
img_Cert_1 = Image.open("images/Solidworks/Ex 223.PNG")
img_Cert_2 = Image.open("images/Solidworks/SW Mill Tut.PNG")
img_Cert_3 = Image.open("images/Solidworks/SW Weld Tut.PNG")
img_Cert_4 = Image.open("images/Solidworks/SW SM Tut.PNG")
img_Cert_5 = Image.open("images/Solidworks/Ex 243.PNG")
img_Cert_6 = Image.open("images/Solidworks/Ex 244.PNG")
video_file_1 = open("videos/SW Assembly1.mp4","rb") 
img_Cert_7 = Image.open("images/Solidworks/SW Weld1.PNG")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("Solidworks Practice 8")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_Cert_7)
with text_column:
    st.subheader("3D Weldment Table")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=_7rzzCVkrMQ)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 7")
    st.write("##")
    video_column, text_column = st.columns((1,2))
    
with video_column:
    video_bytes = video_file_1.read()
    st.video(video_file_1)
with text_column:
    st.subheader("Crane hook model")
    st.write(
        """
         Solidworks Practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=_7rzzCVkrMQ)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 6")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_Cert_6)
with text_column:
    st.subheader("Step drill bit model")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=_7rzzCVkrMQ)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 5")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_Cert_5)
with text_column:
    st.subheader("Solidworks 3D model")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=yKkpFz28bNA)")

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