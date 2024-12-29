import streamlit as st
from PIL import Image
from pathlib import Path
import datetime
import pytz
import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Get the current datetime 
current_datetime = datetime.datetime.now()

# Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday) 
day_of_week = current_datetime.weekday() 

# Map the day of the week to the day name 
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
current_day = days[day_of_week] 

# Display the current 
st.write(f"Today is {current_day}")

def get_user_timezone():
    try:
        # Get user's IP address
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        location = data['loc'].split(',')
        latitude = float(location[0])
        longitude = float(location[1])

        # Get timezone using latitude and longitude
        geolocator = Nominatim(user_agent="timezone_locator")
        location = geolocator.reverse((latitude, longitude), timeout=10)
        timezone_str = location.raw['address']['timezone']
        return timezone_str
    except (requests.exceptions.RequestException, GeocoderTimedOut, KeyError) as e:
        return 'UTC'  # Default to UTC if there's an error

def main():
    st.title("Current Date and Time")

    # Get user's timezone
    user_timezone_str = get_user_timezone()
    user_timezone = pytz.timezone(user_timezone_str)

    # Get current time in user's timezone
    current_datetime = datetime.datetime.now(user_timezone)

    # Display the current date and time
    st.write(f"Current date and time ({user_timezone_str}): {current_datetime}")

if __name__ == "__main__":
    main()

st.title("Hello there!")

# Path settings
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
resume_file = current_dir / "digital cv/assets/CV.pdf"
profile_pic = current_dir / "digital cv/assets/profile-pic.jpg"

# General settings
PAGE_TITLE = "Digital CV | John Mark Casuga"
PAGE_ICON = ":wave:"
NAME = "My Name is John Mark Casuga"
DESCRIPTION = """
A Registered Mechanical Engineer from the Philippines
"""
EMAIL = "casugajohnmark2gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://ph.linkedin.com/in/john-mark-casuga-rmee",
}
CERTIFICATIONS = {
    ""
}

# Load CSS, PDF and PFP
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("Contact me at: casugajohnmark@gmail.com")

# Social links title
st.write("---")
st.write("#")
st.subheader("Social Links")

# Social links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# About this page
st.write("---")
st.write("#")
st.subheader("What's new on this web page?")
custom_css = """
<style>
ul.custom-bullet-points {
    list-style-type: cirlce; /* Change to other types like circle, disc, etc. */
    color: white; /* Change bullet color */
    font-size: 18px; /* Change font size */
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

#change bullet point contents every commit!
st.markdown("""
<ul class="custom-bullet-points">
    <p>Added Thonny Scripts</p>
        <ul>
            <li>added random_story_generator</li>
            <li>added convert_wind_speed</li>
            <li>added pdrop_darcy_weisbach</li>
        </ul>
</ul>
""", unsafe_allow_html=True)
