from pathlib import Path

import streamlit as st
from PIL import Image

# Path settings
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / r"C:\Users\Acer\Streamlit Files\digital cv\styles" / "main.css"
resume_file = current_dir / r"C:\Users\Acer\Streamlit Files\digital cv\assets" / "CV.pdf"
profile_pic = current_dir / r"C:\Users\Acer\Streamlit Files\digital cv\assets" / "profile-pic.jpg"

# General settings
PAGE_TITLE = "Digital CV | John Mark Casuga"
PAGE_ICON = ":wave:"
NAME = "John Mark Casuga"
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

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Hello there!")

# Load CSS, PDF and PFP
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
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
    st.write("casugajohnmark@gmail.com")

# Social links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Experience and Certifications -add link from web page
st.write("#")
st.subheader("Certifications")
st.write(
    """
•Passed the February 2024 Mechanical Engineering Board Exam

•Attained online certifications for Microsoft Office Apps, AutoCAD and Revit

•Completed BOSH/COSH training via Business Enterprise and Career Mentors Inc. 
"""
)

# Skills
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
•2D and 3D CAD: AutoCAD, Revit, Solidworks

•Office Apps: Word, Excel, Powerpoint
"""
)

# Projects
st.write("#")
st.subheader("Projects")
st.write("---")

# Project 1
st.write("Wheeled Agricultural Sprayer (WAS)")
st.write("June 2021-2022")
st.write(
    """
CAPSTONE PROJECT

•	Led team to design and build an Ultra Low Volume (16L) agricultural sprayer with a Field Application Efficiency rate of 85% in dry land condition.

•	Performed design improvements through use of Linkage Mechanism Designer and Simulator and hand calculations.

•	Developed a robust yet sustainable output with a Field Capacity of 2,426 square meter per hour and can be repaired by readily available components.

"""
)