import streamlit as st
from PIL import Image
from pathlib import Path

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

# Optional: Add an overall title for this section
st.header("New Updates for 2025!")
st.divider()

# Creates two columns. You can adjust the ratio if needed, e.g., st.columns([2, 1])
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)

with col1:
    
    st.markdown(
    '<h2><a href="https://casugajm.streamlit.app/.3_Solidworks" target="_self">Solidworks Practice</a></h2>',
    unsafe_allow_html=True)
    st.markdown("""
    * Practice #37 - Deform Model
    * Practice #36 - Triangle Looped Ring
    * Practice #35 - Double Ear Clip
    * Practice #34 - Surface Model
    * Practice #33 - Spiral Volute Shell
    * Practice #32 - Helical Gear Model
    * Practice #31 - Brass Cup Model
    * Practice #30 - Drainage Model
    * Practice #29 - Pattern and Rotate Model
    * Practice #28 - Corrugated Steering Wheel Model
    * Practice #27 - Solidworks 3D Model
    * Practice #26 - Bike Wheel Model
    * Practice #25 - Dice Model
    * Practice #24 - Pump Body Model
    * Practice #23 - Sheet Metal Model
    * Practice #22 - Sheet Metal Rack
    * Practice #21 - Plastic Basket Model
    * Practice #20 - Plastic Mug Model
    * Practice #19 - Solidworks 3D Model
    * Practice #18 - Planetary Gear Model
    * Practice #17 - Universal Joint Model
    * Practice #16 - Solidworks 3D Model
    * Practice #15 - 3D Model of a Plastic Bottle
    * Practice #14 - Sheet Metal CPU Case
    * Practice #13 - 3D Piston model
    * Practice #12 - Drill Vice model
    * Practice #11 - 3D Metal sheet
    * Practice #10 - 3D Weldment beam
    * Practice #9 - 3D Weldment stairs
    * Practice #8 - 3D Weldment table
    * Practice #7 - Crane hook model
    * Practice #6 - Step drill bit model
    * Practice #5 - Solidworks 3D model
    """) # Using a Markdown list

with col2:
    st.markdown(
    '<h2><a href="https://casugajm.streamlit.app/.7_Scripts" target="_self">Scripts</a></h2>',
    unsafe_allow_html=True)
    st.markdown("""
    * Script 4 - Mean Calculator
    * Script 3 - Pressure Drop (Darcy-Weisbach)
    * Script 2 - Wind Speed Converter
    * Script 1 - Random Story Generator
    """) 

with col3:
    st.markdown(
    '<h2><a href="https://casugajm.streamlit.app/.8_Excel" target="_self">Excel Web App</a></h2>',
    unsafe_allow_html=True)
    st.markdown("""
    * Excel Web App 1 - Mock Survey Results filtered by Departments
    * Excel Web App 1 - Mock Survey Table with Sorting
    * Excel Web App 1 - Total number of Participants in each Department
    """)

with col4:
    st.markdown(
    '<h2><a href="https://casugajm.streamlit.app/.2_Certificates" target="_self">Certificates</a></h2>',
    unsafe_allow_html=True)
    st.markdown("""
    * Certificate 11 - Project Management Training and Development
    """)