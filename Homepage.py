import streamlit as st
import datetime
from datetime import datetime, timedelta

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# Page setup
about_page = st.Page(
    page="page/1.1_About me.py",
    title="About Me",
    default=True,
)
project_1_page = st.Page(
    page="page/1.2_Certificates.py",
    title="Certifications",
)
project_2_page = st.Page(
    page="page/2.1_AutoCAD.py",
    title="AutoCAD",
)
project_3_page = st.Page(
    page="page/2.2_Revit.py",
    title="Revit"
)
project_4_page = st.Page(
    page="page/2.3_Solidworks.py",
    title="Solidworks",
)
project_5_page = st.Page(
    page="page/2.4_Capstone.py",
    title="Capstone",
)
project_6_page = st.Page(
    page="page/2.5_Inventor.py",
    title="Inventor"
)
project_7_page = st.Page(
    page="page/2.6_Blender Renders.py",
    title="Blender Renders"
)
project_8_page = st.Page(
    page="page/2.7_Scripts.py",
    title="Scripts"
)


# Navigation setup without sections
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# Navigation setup with sections
pg = st.navigation(
    {
        "Info": [about_page, project_1_page],
        "Projects": [project_2_page, project_7_page, project_5_page, project_6_page, project_3_page, project_8_page, project_4_page],
    }
)

# Load your audio file
audio_file = "audio/Nuvolebianche.ogg"

# Display the audio player
st.audio(audio_file, loop=True, autoplay=True)

# Function to get the current time in UTC +8
def get_current_time():
    utc_now = datetime.utcnow()
    utc_plus_8 = utc_now + timedelta(hours=8)
    return utc_plus_8.strftime('%A, %B %d, %Y %H:%M:%S')

# Display the current time in UTC +8
current_time = get_current_time()
st.markdown(f'<div class="clock-container">{current_time}</div>', unsafe_allow_html=True)

# Shared assets
st.logo("assets/gear.png")
st.sidebar.text("Made by yours truly ❤ ")

# Run navigation
pg.run()