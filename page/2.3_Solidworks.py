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
img_Cert_29 = Image.open("images/Solidworks/Pattern and Rotate.PNG")
img_Cert_30 = Image.open("images/Solidworks/Holes with Instances.PNG")
img_Cert_31 = Image.open("images/Solidworks/Brass Cup.PNG")
img_Cert_32 = Image.open("images/Solidworks/Helical Gear.PNG")
img_Cert_33 = Image.open("images/Solidworks/Spiral Volute Shell.PNG")
img_Cert_34 = Image.open("images/Solidworks/Surface Modelling 1.PNG")
img_Cert_35 = Image.open("images/Solidworks/Double Ear Clip.PNG")
img_Cert_36 = Image.open("images/Solidworks/Triangle Looped Ring.PNG")
img_Cert_37 = Image.open("images/Solidworks/Deform Model 1.PNG")
img_Cert_38 = Image.open("images/Solidworks/Circular Shaped Spring.PNG")
img_Cert_39 = Image.open("images/Solidworks/Carabinet Model.PNG")
img_Cert_40 = Image.open("images/Solidworks/Exhaust Manifold Model.PNG")
img_Cert_40_1 = Image.open("images/Solidworks/Exhaust Manifold Model.2.PNG")
img_Cert_40_2 = Image.open("images/Solidworks/Exhaust Manifold Model.3.PNG")
img_Cert_41 = Image.open("images/Solidworks/Drill Bit Model.PNG")
img_Cert_42 = Image.open("images/Solidworks/Tri-corner Trophy Model.PNG")
img_Cert_43 = Image.open("images/Solidworks/5 Tines Rake Model.PNG")
img_Cert_44 = Image.open("images/Solidworks/Claw Hammer Model.PNG")
img_Cert_45 = Image.open("images/Solidworks/Volvo Wheel Loader Model.PNG")
img_Cert_45_1 = Image.open("images/Solidworks/Volvo Wheel Loader Model2.PNG")
video_file_6 = open("videos/Volvo Wheel Loader Model.mp4","rb")
img_Cert_46 = Image.open("images/Solidworks/Honeycomb Mesh Model.PNG")
img_Cert_47 = Image.open("images/Solidworks/Gear Fidget Spinner.PNG")
img_Cert_48 = Image.open("images/Solidworks/Light Bulb Model.PNG")
img_Cert_49 = Image.open("images/Solidworks/Rubber Handle Model.PNG")
img_Cert_50 = Image.open("images/Solidworks/Hair Dryer Nozzle Model.PNG")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("Solidworks Practice 50")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_50)  
with text_column:
    st.subheader("Hair Dryer Nozzle Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=3K1eCxUAqkM&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=2)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 49")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_49)  
with text_column:
    st.subheader("Rubber Handle Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=GUuNgJo-4g0&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=3)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 48")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_48)  
with text_column:
    st.subheader("Light Bulb Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=Tu0dfx7d2OQ&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=14)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 47")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_47)  
with text_column:
    st.subheader("Gear Fidget Spinner")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=GH7obM6TL3k&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=9)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 46")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_46)  
with text_column:
    st.subheader("Honeycomb Mesh Model")
    st.write(
        """
         Solidworks practice from Solidworks Central
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=TeqXivG8SIU&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=22)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 45")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_45)
    st.image(img_Cert_45_1)
    st.video(video_file_6)
    video_bytes = video_file_6.read()   
with text_column:
    st.subheader("Volvo Wheel Loader Model")
    st.write(
        """
         Solidworks practice
        """
        )
    st.markdown("[Learn from here...]()")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 44")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_44)
with text_column:
    st.subheader("Claw Hammer Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=MZmIM0MWlhs&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=18)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 43")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_43)
with text_column:
    st.subheader("5 Tines Rake Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=u0KpRaV8J4k&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=47)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 42")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_42)
with text_column:
    st.subheader("Tri-Corner Trophy Model")
    st.write(
        """
         Solidworks practice from SolidWorks Central
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=2F0jTUPycIw&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=3)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 41")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_41)
with text_column:
    st.subheader("Drill Bit Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=yNt9vzxjXB0&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=4)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 40")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_40)
    st.image(img_Cert_40_1)
    st.image(img_Cert_40_2)
with text_column:
    st.subheader("Exhaust Manifold Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=YCuqkoN1nAs)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 39")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_39)
with text_column:
    st.subheader("Carabinet Model")
    st.write(
        """
         Solidworks practice from 3D World
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=SQwUya2Y4sc&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=6)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 38")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_38)
with text_column:
    st.subheader("Circular Shaped Spring")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=7Q602vk0TWM&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 37")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_37)
with text_column:
    st.subheader("Deform Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=EMzLF5w3pAI&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=34)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 36")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_36)
with text_column:
    st.subheader("Triangle Looped Ring")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=EVBKVX1r18c&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=16)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 35")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_35)
with text_column:
    st.subheader("Double Ear Clip")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=t-e3cuBgArU)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 34")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_34)
with text_column:
    st.subheader("Surface Model")
    st.write(
        """
         Solidworks practice from Cadmake
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=yFED4qHR0IA)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 33")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_33)
with text_column:
    st.subheader("Spiral Volute Shell")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=0sduhyJWtEY&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=8)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 32")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_32)
with text_column:
    st.subheader("Helical Gear Model")
    st.write(
        """
         Solidworks practice from Cadmake
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=e_0CHSRfoQ4&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=10)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 31")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_31)
with text_column:
    st.subheader("Brass Cup Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=fpnvddI_Tck&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=2)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 30")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_30)
with text_column:
    st.subheader("Drainage Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=NvLDB_Eu2BI&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=6)")

with st.container():
    st.write("---")
    st.header("Solidworks Practice 29")
    st.write("##")
    image_column, text_column = st.columns((2,2))

with image_column:
    st.image(img_Cert_29)
with text_column:
    st.subheader("Pattern and Rotate Model")
    st.write(
        """
         Solidworks practice from Mahtabalam
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=-MJhwaQQU_E)")

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