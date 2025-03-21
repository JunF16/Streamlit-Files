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

#add bullet point contents every commit!
st.markdown("""
<ul class="custom-bullet-points">
    <p>New update for 2025 includes:</p>
        <ul>
            <li>Solidworks Practice #13 - 3D Piston model</li>
            <li>Solidworks Practice #12 - Drill Vice model</li>
            <li>Solidworks Practice #11 - 3D Metal sheet</li>
            <li>Solidworks Practice #10 - 3D Weldment beam</li>
            <li>Solidworks Practice #9 - 3D Weldment stairs</li>
            <li>Solidworks Practice #8 - 3D Weldment table</li>
            <li>Solidworks Practice #7 - Crane hook model</li>
            <li>Solidworks Practice #6 - Step drill bit model</li>
            <li>Solidworks Practice #5 - Solidworks 3D model</li>
            <li>Thonny Scripts 3 - Pressure Drop using Darcy-Weisbach Equation</li>
            <li>Thonny Scripts 2 - Wind Speed Converter</li>
            <li>Thonny Scripts 1 - Random Story Generator</li>
        </ul>
</ul>
""", unsafe_allow_html=True)
