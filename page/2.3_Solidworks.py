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
img_Cert_8 = Image.open("images/Solidworks/SW Weld2.PNG")
img_Cert_9 = Image.open("images/Solidworks/SW Weld3.PNG")
img_Cert_10 = Image.open("images/Solidworks/SW Weld4.PNG")
video_file_2 = open("videos/SW Assembly2.mp4","rb")
img_Cert_11 = Image.open("images/Solidworks/SW Piston.PNG")
img_Cert_12 = Image.open("images/Solidworks/SW SM CPU Case.PNG")
img_Cert_13 = Image.open("images/Solidworks/SW SM CPU Case2.PNG")
img_Cert_14 = Image.open("images/Solidworks/SW Plastic Bottle.PNG")
img_Cert_15 = Image.open("images/Solidworks/SW Plastic Bottle1.PNG")
img_Cert_16 = Image.open("images/Solidworks/SW Plastic Bottle2.PNG")
img_Cert_17 = Image.open("images/Solidworks/Ex 130.PNG")
video_file_3 = open("videos/SW Assembly4.mp4","rb")
video_file_4 = open("videos/SW Assembly5.mp4","rb")
video_file_5 = open("videos/SW Assembly5.2.mp4","rb")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("Solidworks Practice 18")
    st.write("##")
    video_column, text_column = st.columns((2,2))
    
with video_column:
    video_bytes = video_file_4.read()
    st.video(video_file_4)
    video_bytes = video_file_5.read()
    st.video(video_file_5)
with text_column:
    st.subheader("Planetary Gear Model")
    st.write(
        """
         Solidworks Practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=2mBRTeEtsv4&t=3075s)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 17")
    st.write("##")
    video_column, text_column = st.columns((2,2))
    
with video_column:
    video_bytes = video_file_3.read()
    st.video(video_file_3)
with text_column:
    st.subheader("Universal Joint Model")
    st.write(
        """
         Solidworks Practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=X7ZV9oKXIXA)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 16")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_17)
with text_column:
    st.subheader("Solidworks 3D Model")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=NC5IN35bBvo)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 15")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_14)
    st.image(img_Cert_15)
    st.image(img_Cert_16)
with text_column:
    st.subheader("3D Model of a Plastic Bottle")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=yK52E8bZD-s)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 14")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_12)
    st.image(img_Cert_13)
with text_column:
    st.subheader("Sheet Metal CPU Case")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=H17nr57bxsM&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 13")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_11)
with text_column:
    st.subheader("3D Piston model")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=a9dpWeGBWfU)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 12")
    st.write("##")
    video_column, text_column = st.columns((2,2))
    
with video_column:
    video_bytes = video_file_2.read()
    st.video(video_file_2)
with text_column:
    st.subheader("Drill vice model")
    st.write(
        """
         Solidworks Practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=X7ZV9oKXIXA)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 11")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_10)
with text_column:
    st.subheader("3D Metal Sheet")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=KMXm8H2hynI)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 10")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_9)
with text_column:
    st.subheader("3D Weldment Beam")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=PUTo-HForow)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 9")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_8)
with text_column:
    st.subheader("3D Weldment Stairs")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=BMlsOO6eFxs)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 8")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_7)
with text_column:
    st.subheader("3D Weldment Table")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=u1esUuvivoo)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 7")
    st.write("##")
    video_column, text_column = st.columns((2,2))
    
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
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=XXZSOqtRO6s)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 6")
    st.write("##")
    image_column, text_column = st.columns((2,2))

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
    image_column, text_column = st.columns((2,2))

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
    image_column, text_column = st.columns((2,2))
    
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
    image_column, text_column = st.columns((2,2))
    
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
    image_column, text_column = st.columns((2,2))
    
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
    image_column, text_column = st.columns((2,2))
    
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