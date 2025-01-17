import streamlit as st
import os
import datetime
import pytz
import requests
from timezonefinder import TimezoneFinder
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

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
    page="page/2.7_Thonny Scripts.py",
    title="Thonny Scripts"
)


# Navigation setup without sections
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# Navigation setup with sections
pg = st.navigation(
    {
        "Info": [about_page, project_1_page],
        "Projects": [project_2_page, project_7_page, project_5_page, project_6_page, project_3_page, project_4_page, project_8_page],
    }
)

# Load your audio file
audio_file = "audio/Nuvolebianche.ogg"

# Display the audio player
st.audio(audio_file, loop=True, autoplay=True)

def get_user_location():
    try:
        # Get user's IP address and location data
        with st.expander("View IP Info Response"):
            response = requests.get('https://ipinfo.io/json')
            st.write("IP Info Response:", response.json())  # Log the response
            data = response.json()
            location = data['loc'].split(',')
            latitude = float(location[0])
            longitude = float(location[1])
            return latitude, longitude
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

def get_user_timezone(lat, lon):
    try:
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lat=lat, lng=lon)
        if timezone_str is None:
            timezone_str = 'UTC'  # Default to UTC if timezone is not found
        return timezone_str
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return 'UTC'  # Default to UTC if there's an error

def main():
    st.markdown(
    """
    <style>
    .big-font {
        font-size:18px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    st.markdown('<p class="big-font">Current Date and Time</p>', unsafe_allow_html=True)

    # Get user's location
    location = get_user_location()
    if location:
        latitude, longitude = location
        # Get user's timezone
        user_timezone_str = get_user_timezone(latitude, longitude)
        user_timezone = pytz.timezone(user_timezone_str)

        # Get current time in user's timezone
        current_datetime = datetime.datetime.now(user_timezone)
        
        # Display the current date and time
        st.write(f"Current date and time ({user_timezone_str}): {current_datetime}")
    else:
        st.write("Unable to determine location and timezone.")

if __name__ == "__main__":
    main()


# Get the current date and time 
current_datetime = datetime.datetime.now()

# Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday) 
day_of_week = current_datetime.weekday() 

# Map the day of the week to the day name 
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
current_day = days[day_of_week] 

# Display the current day 
st.write(f"Today is {current_day}")

# Shared assets
st.logo("assets/gear.png")
st.sidebar.text("Made by yours truly ❤ ")

# Run navigation
pg.run()