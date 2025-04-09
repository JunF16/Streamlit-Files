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

# --- Populate the first column (Solidworks) ---
with col1:
    st.subheader("Solidworks Practice") # Heading for the first column
    st.markdown("""
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

# --- Populate the second column (Thonny Scripts) ---
with col2:
    st.subheader("Scripts") # Heading for the second column
    st.markdown("""
    * Script 4 - Mean Calculator
    * Script 3 - Pressure Drop (Darcy-Weisbach)
    * Script 2 - Wind Speed Converter
    * Script 1 - Random Story Generator
    """) # Using a Markdown list

# You can add more content below the columns if needed
# st.write("More updates coming soon...")
