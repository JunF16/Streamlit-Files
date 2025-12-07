from PIL import Image
import streamlit as st
from pathlib import Path
from typing import List, Optional, Dict, Any
import math

# --- Helper Function to Display a Project ---
def display_project(
    # ... (function arguments remain the same)
    header: str,
    subheader: str,
    description: str,
    learn_more_link: str,
    image_paths: Optional[List[Path]] = None,
    video_paths: Optional[List[Path]] = None,
    model_link: Optional[str] = None,
):
    """Creates a container for a project, loading assets lazily."""
    with st.container():
        st.write("---")
        st.header(header)
        st.write("##")
        left_column, right_column = st.columns((2, 2))
        
        with left_column:
            if image_paths:
                # If there's more than one image, create a slider
                if len(image_paths) > 1:
                    slider_key = f"slider_{header.replace(' ', '_')}"
                    slider_label = f"{subheader} Renders"
                    idx = st.slider(slider_label, 1, len(image_paths), 1, key=slider_key)
                    st.image(Image.open(image_paths[idx - 1]), use_column_width=True)
                else:
                    st.image(Image.open(image_paths[0]), use_column_width=True)
            
            if video_paths:
                for video_path in video_paths:
                    # Pass the file path directly for efficient streaming
                    st.video(str(video_path))

        with right_column:
            st.subheader(subheader)
            st.write(description)
            st.markdown(f"[Learn from here...]({learn_more_link})")
            if model_link:
                st.markdown(f"[Download my model here...]({model_link})")

# --- Asset Path Setup ---
IMG_DIR = Path("images/Solidworks")
VID_DIR = Path("videos")

# --- Project Data (Populate this list with all your projects) ---
PROJECT_DATA: List[Dict[str, Any]] = [
    { "header": "Solidworks Practice 62", "subheader": "Flathead Screwdriver Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=-NB-NR1_0Do&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=5", "image_paths": [IMG_DIR / "Flathead Screwdriver.PNG"], },
    { "header": "Solidworks Practice 61", "subheader": "Corkscrew Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=Ybiu0QqShDA&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=13", "image_paths": [IMG_DIR / "Corkscrew Model.PNG"], },
    {
        "header": "Solidworks Practice 60",
        "subheader": "Plastic Organizer Assembly",
        "description": "Solidworks practice from GrabCAD",
        "learn_more_link": "https://grabcad.com/library/small-parts-organizer-1",
        "image_paths": [
            IMG_DIR / "Plastic Organizer Assembly.PNG",
            IMG_DIR / "Plastic Organizer Assembly2.PNG",
        ],
    },
    {
        "header": "Solidworks Practice 59",
        "subheader": "Laptop Stand Model",
        "description": "Solidworks practice from GrabCAD",
        "learn_more_link": "https://grabcad.com/library/small-parts-organizer-1",
        "image_paths": [IMG_DIR / "Laptop Stand Model.PNG", IMG_DIR / "Laptop Stand Model2.PNG"],
    },
    {
        "header": "Solidworks Practice 58",
        "subheader": "Table Fan Model",
        "description": "Solidworks practice from GrabCAD",
        "learn_more_link": "https://grabcad.com/library/mini-table-fan-2",
        "image_paths": [IMG_DIR / "Table Fan Model.PNG", IMG_DIR / "Table Fan Model2.PNG"],
    },
    {
        "header": "Solidworks Practice 57",
        "subheader": "Rubik's Cube Model",
        "description": "Solidworks practice from Manjeet Singh",
        "learn_more_link": "https://www.youtube.com/watch?v=BT_ksVYtfWM&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=9",
        "image_paths": [IMG_DIR / "Rubiks Cube.PNG"],
    },
    {
        "header": "Solidworks Practice 56",
        "subheader": "Screw Lift Podium",
        "description": "Solidworks practice from SKY-CAD-TECHNOLOGY",
        "learn_more_link": "https://www.youtube.com/watch?v=Ep8TltUEmwA&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=12",
        "image_paths": [IMG_DIR / "Screw Lift Podium.PNG"],
        "video_paths": [VID_DIR / "Screw Lift Podium.mp4"],
    },
    {
        "header": "Solidworks Practice 55",
        "subheader": "Wooden Bench Model",
        "description": "Solidworks practice from Mahtabalam",
        "learn_more_link": "https://www.youtube.com/watch?v=CvG9gtiLiFM&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=4",
        "image_paths": [IMG_DIR / "Wooden Bench.PNG", IMG_DIR / "Wooden Bench2.PNG", IMG_DIR / "Wooden Bench3.PNG"],
    },
    {
        "header": "Solidworks Practice 54",
        "subheader": "Windshield Grid Model",
        "description": "Solidworks practice from Mahtabalam",
        "learn_more_link": "https://www.youtube.com/watch?v=O4tY9rygihY&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=13",
        "image_paths": [IMG_DIR / "Windshield Grid Model.PNG"],
    },
    {
        "header": "Solidworks Practice 53",
        "subheader": "Exercise 258",
        "description": "Solidworks practice from Mahtabalam",
        "learn_more_link": "https://www.youtube.com/watch?v=HBK-ZVYrIpU&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=12",
        "image_paths": [IMG_DIR / "Ex 258.PNG"],
    },
    {
        "header": "Solidworks Practice 52",
        "subheader": "Off-road Buggy Model",
        "description": "Solidworks practice from Fully Defined",
        "learn_more_link": "https://www.youtube.com/watch?v=SPvlJ5xVVmg&list=PLBzmroCxoKwyWP86rzB4AUOUM_wUrEPir",
        "image_paths": [IMG_DIR / "Off Road Buggy Brick Model.PNG"],
    },
    {
        "header": "Solidworks Practice 51",
        "subheader": "Lifting Ring Model",
        "description": "Solidworks practice from Mahtabalam",
        "learn_more_link": "https://www.youtube.com/watch?v=TGodt8O88EI&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=3&pp=gAQBiAQB",
        "image_paths": [IMG_DIR / "Lifting Ring Model.PNG"],
    },
    {
        "header": "Solidworks Practice 50",
        "subheader": "Hair Dryer Nozzle Model",
        "description": "Solidworks practice from Mahtabalam",
        "learn_more_link": "https://www.youtube.com/watch?v=3K1eCxUAqkM&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=2",
        "image_paths": [IMG_DIR / "Hair Dryer Nozzle Model.PNG"],
    },
    {
        "header": "Solidworks Practice 49",
        "subheader": "Rubber Handle Model",
        "description": "Solidworks practice from Mahtabalam",
        "learn_more_link": "https://www.youtube.com/watch?v=GUuNgJo-4g0&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=3",
        "image_paths": [IMG_DIR / "Rubber Handle Model.PNG"],
    },
    {
        "header": "Solidworks Practice 48",
        "subheader": "Light Bulb Model",
        "description": "Solidworks practice from Mahtabalam",
        "learn_more_link": "https://www.youtube.com/watch?v=Tu0dfx7d2OQ&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=14",
        "image_paths": [IMG_DIR / "Light Bulb Model.PNG"],
    },
    {
        "header": "Solidworks Practice 47",
        "subheader": "Gear Fidget Spinner",
        "description": "Solidworks practice from Mahtabalam",
        "learn_more_link": "https://www.youtube.com/watch?v=GH7obM6TL3k&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=9",
        "image_paths": [IMG_DIR / "Gear Fidget Spinner.PNG"],
    },
    {
        "header": "Solidworks Practice 46",
        "subheader": "Honeycomb Mesh Model",
        "description": "Solidworks practice from Solidworks Central",
        "learn_more_link": "https://www.youtube.com/watch?v=TeqXivG8SIU&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=22",
        "image_paths": [IMG_DIR / "Honeycomb Mesh Model.PNG"],
    },
    {
        "header": "Solidworks Practice 45",
        "subheader": "Volvo Wheel Loader Model",
        "description": "Solidworks practice from Fully Defined",
        "learn_more_link": "https://www.youtube.com/@FullyDefined-Design",
        "image_paths": [IMG_DIR / "Volvo Wheel Loader Model.PNG", IMG_DIR / "Volvo Wheel Loader Model2.PNG"],
        "video_paths": [VID_DIR / "Volvo Wheel Loader Model.mp4"],
    },
    { "header": "Solidworks Practice 44", "subheader": "Claw Hammer Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=MZmIM0MWlhs&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=18", "image_paths": [IMG_DIR / "Claw Hammer Model.PNG"], },
    { "header": "Solidworks Practice 43", "subheader": "5 Tines Rake Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=u0KpRaV8J4k&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=47", "image_paths": [IMG_DIR / "5 Tines Rake Model.PNG"], },
    { "header": "Solidworks Practice 42", "subheader": "Tri-Corner Trophy Model", "description": "Solidworks practice from SolidWorks Central", "learn_more_link": "https://www.youtube.com/watch?v=2F0jTUPycIw&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=3", "image_paths": [IMG_DIR / "Tri-corner Trophy Model.PNG"], },
    { "header": "Solidworks Practice 41", "subheader": "Drill Bit Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=yNt9vzxjXB0&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=4", "image_paths": [IMG_DIR / "Drill Bit Model.PNG"], },
    { "header": "Solidworks Practice 40", "subheader": "Exhaust Manifold Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=YCuqkoN1nAs", "image_paths": [IMG_DIR / "Exhaust Manifold Model.PNG", IMG_DIR / "Exhaust Manifold Model.2.PNG", IMG_DIR / "Exhaust Manifold Model.3.PNG"], },
    { "header": "Solidworks Practice 39", "subheader": "Carabinet Model", "description": "Solidworks practice from 3D World", "learn_more_link": "https://www.youtube.com/watch?v=SQwUya2Y4sc&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=6", "image_paths": [IMG_DIR / "Carabinet Model.PNG"], },
    { "header": "Solidworks Practice 38", "subheader": "Circular Shaped Spring", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=7Q602vk0TWM&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD", "image_paths": [IMG_DIR / "Circular Shaped Spring.PNG"], },
    { "header": "Solidworks Practice 37", "subheader": "Deform Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=EMzLF5w3pAI&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=34", "image_paths": [IMG_DIR / "Deform Model 1.PNG"], },
    { "header": "Solidworks Practice 36", "subheader": "Triangle Looped Ring", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=EVBKVX1r18c&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=16", "image_paths": [IMG_DIR / "Triangle Looped Ring.PNG"], },
    { "header": "Solidworks Practice 35", "subheader": "Double Ear Clip", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=t-e3cuBgArU", "image_paths": [IMG_DIR / "Double Ear Clip.PNG"], },
    { "header": "Solidworks Practice 34", "subheader": "Surface Model", "description": "Solidworks practice from Cadmake", "learn_more_link": "https://www.youtube.com/watch?v=yFED4qHR0IA", "image_paths": [IMG_DIR / "Surface Modelling 1.PNG"], },
    { "header": "Solidworks Practice 33", "subheader": "Spiral Volute Shell", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=0sduhyJWtEY&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=8", "image_paths": [IMG_DIR / "Spiral Volute Shell.PNG"], },
    { "header": "Solidworks Practice 32", "subheader": "Helical Gear Model", "description": "Solidworks practice from Cadmake", "learn_more_link": "https://www.youtube.com/watch?v=e_0CHSRfoQ4&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=10", "image_paths": [IMG_DIR / "Helical Gear.PNG"], },
    { "header": "Solidworks Practice 31", "subheader": "Brass Cup Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=fpnvddI_Tck&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=2", "image_paths": [IMG_DIR / "Brass Cup.PNG"], },
    { "header": "Solidworks Practice 30", "subheader": "Drainage Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=NvLDB_Eu2BI&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=6", "image_paths": [IMG_DIR / "Holes with Instances.PNG"], },
    { "header": "Solidworks Practice 29", "subheader": "Pattern and Rotate Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=-MJhwaQQU_E", "image_paths": [IMG_DIR / "Pattern and Rotate.PNG"], },
    { "header": "Solidworks Practice 28", "subheader": "Corrugated Steering Wheel Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=XxiXdzR07Yw&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=4", "image_paths": [IMG_DIR / "Corrugated Wheel.PNG"], },
    { "header": "Solidworks Practice 27", "subheader": "Solidworks 3D Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=_WeXUfN94O8&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD&index=10", "image_paths": [IMG_DIR / "Ex 256.PNG"], },
    { "header": "Solidworks Practice 26", "subheader": "Bike Tire and Rim", "description": "Solidworks practice from CAD Monkeys", "learn_more_link": "https://www.youtube.com/watch?v=VlqgIK81pgI", "image_paths": [IMG_DIR / "Bike Tire n Rim.PNG"], },
    { "header": "Solidworks Practice 25", "subheader": "Dice Model", "description": "Solidworks practice from Mahtabalam", "learn_more_link": "https://www.youtube.com/watch?v=kflJzTSUwqE", "image_paths": [IMG_DIR / "SW Dice Model.PNG"], },
    { "header": "Solidworks Practice 24", "subheader": "Pump Body Model", "description": "Solidworks practice from Too Tall Toby", "learn_more_link": "https://www.youtube.com/watch?v=cbCkNIb4zPw", "image_paths": [IMG_DIR / "SW Pump Body TTT.PNG"], },
    { "header": "Solidworks Practice 23", "subheader": "Sheet Metal Model", "description": "Solidworks practice from Too Tall Toby", "learn_more_link": "https://www.youtube.com/watch?v=o64aMeDdKsw&list=WL&index=3", "image_paths": [IMG_DIR / "SW SM 01 TTT.PNG"], },
    { "header": "Solidworks Practice 22", "subheader": "Sheet Metal Rack", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=RLJ_dbMl8fk", "image_paths": [IMG_DIR / "SW SM Metal Rack.PNG", IMG_DIR / "SM Metal Rack DXF.PNG"], },
    { "header": "Solidworks Practice 21", "subheader": "Plastic Basket Model", "description": "Solidworks practice from Solid House", "learn_more_link": "https://www.youtube.com/watch?v=UkQBsB0PnDo", "image_paths": [IMG_DIR / "SW Plastic Basket.PNG"], },
    { "header": "Solidworks Practice 20", "subheader": "Plastic Mug Model", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=bboMwvwOYLE", "image_paths": [IMG_DIR / "SW Plastic Mug.PNG"], },
    { "header": "Solidworks Practice 19", "subheader": "Solidworks 3D Model", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=yF6eHOR1JDM", "image_paths": [IMG_DIR / "Ex 252.PNG", IMG_DIR / "Ex 252.1.PNG"], },
    { "header": "Solidworks Practice 18", "subheader": "Planetary Gear Model", "description": "Solidworks Practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=2mBRTeEtsv4&t=3075s", "video_paths": [VID_DIR / "SW Assembly5.mp4", VID_DIR / "SW Assembly5.2.mp4"], },
    { "header": "Solidworks Practice 17", "subheader": "Universal Joint Model", "description": "Solidworks Practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=X7ZV9oKXIXA", "video_paths": [VID_DIR / "SW Assembly4.mp4"], },
    { "header": "Solidworks Practice 16", "subheader": "Solidworks 3D Model", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=NC5IN35bBvo", "image_paths": [IMG_DIR / "Ex 130.PNG"], },
    { "header": "Solidworks Practice 15", "subheader": "3D Model of a Plastic Bottle", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=yK52E8bZD-s", "image_paths": [IMG_DIR / "SW Plastic Bottle.PNG", IMG_DIR / "SW Plastic Bottle1.PNG", IMG_DIR / "SW Plastic Bottle2.PNG"], },
    { "header": "Solidworks Practice 14", "subheader": "Sheet Metal CPU Case", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=H17nr57bxsM&list=PL6ZitbPhhYsTfuoGXgsTknh-YfSf0T4zD", "image_paths": [IMG_DIR / "SW SM CPU Case.PNG", IMG_DIR / "SW SM CPU Case2.PNG"], },
    { "header": "Solidworks Practice 13", "subheader": "3D Piston model", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=a9dpWeGBWfU", "image_paths": [IMG_DIR / "SW Piston.PNG"], },
    { "header": "Solidworks Practice 12", "subheader": "Drill vice model", "description": "Solidworks Practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=X7ZV9oKXIXA", "video_paths": [VID_DIR / "SW Assembly2.mp4"], },
    { "header": "Solidworks Practice 11", "subheader": "3D Metal Sheet", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=KMXm8H2hynI", "image_paths": [IMG_DIR / "SW Weld4.PNG"], },
    { "header": "Solidworks Practice 10", "subheader": "3D Weldment Beam", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=PUTo-HForow", "image_paths": [IMG_DIR / "SW Weld3.PNG"], },
    { "header": "Solidworks Practice 9", "subheader": "3D Weldment Stairs", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=BMlsOO6eFxs", "image_paths": [IMG_DIR / "SW Weld2.PNG"], },
    { "header": "Solidworks Practice 8", "subheader": "3D Weldment Table", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=u1esUuvivoo", "image_paths": [IMG_DIR / "SW Weld1.PNG"], },
    { "header": "Solidworks Practice 7", "subheader": "Crane hook model", "description": "Solidworks Practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=XXZSOqtRO6s", "video_paths": [VID_DIR / "SW Assembly1.mp4"], },
    { "header": "Solidworks Practice 6", "subheader": "Step drill bit model", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=_7rzzCVkrMQ", "image_paths": [IMG_DIR / "Ex 244.PNG"], },
    { "header": "Solidworks Practice 5", "subheader": "Solidworks 3D model", "description": "Solidworks practice from MAHTABALAM", "learn_more_link": "https://www.youtube.com/watch?v=yKkpFz28bNA", "image_paths": [IMG_DIR / "Ex 243.PNG"], },
    { "header": "Solidworks Practice 4", "subheader": "Solidworks Sheet Metal Model", "description": "Solidworks practice from Solidworks Tutorial", "learn_more_link": "[Learn from built-in Solidworks Tutorial]", "image_paths": [IMG_DIR / "SW SM Tut.PNG"], },
    { "header": "Solidworks Practice 3", "subheader": "Solidworks Weldment Model", "description": "Solidworks practice from Solidworks Tutorial", "learn_more_link": "[Learn from built-in Solidworks Tutorial]", "image_paths": [IMG_DIR / "SW Weld Tut.PNG"], },
    { "header": "Solidworks Practice 2", "subheader": "Solidworks Mill Model", "description": "Solidworks practice from Solidworks Tutorial", "learn_more_link": "[Learn from built-in Solidworks Tutorial]", "image_paths": [IMG_DIR / "SW Mill Tut.PNG"], },
    {
        "header": "Solidworks Practice 1",
        "subheader": "Solidworks 3D model",
        "description": "Solidworks practice from MAHTABALAM",
        "learn_more_link": "https://www.youtube.com/watch?v=fFZTvQjRnyY",
        "model_link": "#",  # Add your download link here
        "image_paths": [IMG_DIR / "Ex 223.PNG"],
    },
]

# --- Pagination Logic ---
projects_per_page = 10  # You can adjust this number
total_projects = len(PROJECT_DATA)
total_pages = math.ceil(total_projects / projects_per_page)

# Get current page number from user input
page_number = st.selectbox(
    "Select Page",
    options=list(range(1, total_pages + 1)),
    format_func=lambda x: f"Page {x}",
    key="solidworks_page_selector"
)

# Calculate the start and end index for the projects to display on the current page
start_index = (page_number - 1) * projects_per_page
end_index = start_index + projects_per_page

# Get the projects for the current page
projects_to_display = PROJECT_DATA[start_index:end_index]

# --- Display Projects for the Current Page ---
for project in projects_to_display:
    display_project(
        header=project["header"],
        subheader=project["subheader"],
        description=project["description"],
        learn_more_link=project["learn_more_link"],
        image_paths=project.get("image_paths"),
        video_paths=project.get("video_paths"),
        model_link=project.get("model_link"),
    )