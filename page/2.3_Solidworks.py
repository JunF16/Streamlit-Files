from PIL import Image
import streamlit as st
from pathlib import Path

# Load Assets (add underscore for image version under same item)
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
img_Cert_18 = Image.open("images/Solidworks/Ex 252.PNG")
img_Cert_19 = Image.open("images/Solidworks/Ex 252.1.PNG")
img_Cert_20 = Image.open("images/Solidworks/SW Plastic Mug.PNG")
img_Cert_21 = Image.open("images/Solidworks/SW Plastic Basket.PNG")
img_Cert_22 = Image.open("images/Solidworks/SW SM Metal Rack.PNG")
img_Cert_22_1 = Image.open("images/Solidworks/SM Metal Rack DXF.PNG")
img_Cert_23 = Image.open("images/Solidworks/SW SM 01 TTT.PNG")
img_Cert_24 = Image.open("images/Solidworks/SW Pump Body TTT.PNG")
img_Cert_25 = Image.open("images/Solidworks/SW Dice Model.PNG")
img_Cert_26 = Image.open("images/Solidworks/Bike Tire n Rim.PNG")
img_Cert_27 = Image.open("images/Solidworks/Ex 256.PNG")
img_Cert_28 = Image.open("images/Solidworks/Corrugated Wheel.PNG")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("Solidworks Practice 28")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_28)
with text_column:
    st.subheader("Corrugated Steering Wheel Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=XxiXdzR07Yw&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=4)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 27")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_27)
with text_column:
    st.subheader("Solidworks 3D Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=_WeXUfN94O8&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=10)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 26")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_26)
with text_column:
    st.subheader("Bike Tire and Rim")
    st.write(
        """
         Solidworks practice from CAD Monkeys
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=VlqgIK81pgI)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 25")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_25)
with text_column:
    st.subheader("Dice Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=kflJzTSUwqE)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 24")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_24)
with text_column:
    st.subheader("Pump Body Model")
    st.write(
        """
         Solidworks practice from Too Tall Toby
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=cbCkNIb4zPw)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 23")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_23)
with text_column:
    st.subheader("Sheet Metal Model")
    st.write(
        """
         Solidworks practice from Too Tall Toby
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=o64aMeDdKsw&list=WL&index=3)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 22")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_22)
    st.image(img_Cert_22_1)
with text_column:
    st.subheader("Sheet Metal Rack")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=RLJ_dbMl8fk)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 21")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_21)
with text_column:
    st.subheader("Plastic Basket Model")
    st.write(
        """
         Solidworks practice from Solid House
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=UkQBsB0PnDo)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 20")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_20)
with text_column:
    st.subheader("Plastic Mug Model")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=bboMwvwOYLE)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 19")
    st.write("##")
    image_column, text_column = st.columns((2,2))
with image_column:
    st.image(img_Cert_18)
    st.image(img_Cert_19)
with text_column:
    st.subheader("Solidworks 3D Model")
    st.write(
        """
         Solidworks practice from MAHTABALAM
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=yF6eHOR1JDM)")

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