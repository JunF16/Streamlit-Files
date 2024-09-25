import streamlit as st
from PIL import Image
from pathlib import Path

st.title("Hello there!")

# Path settings
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
resume_file = current_dir / r"C:\Users\Acer\Streamlit Files\digital cv\assets" / "CV.pdf"
profile_pic = current_dir / r"C:\Users\Acer\Streamlit Files\digital cv\assets" / "profile-pic.jpg"

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
st.subheader("ℹ [About this web page]")
st.write(
   """
            I created this web page to share my progress in learning various tools in 2D and 3D CAD modelling softwares. 
            I also post practice files I found interesting on Youtube which may include tutorials.

            What you'll see on this web page:

               ⚙ My 2D and 3D renders from Solidworks, Revit and AutoCAD

               ⚙ Various practice files I found from Youtube

               ⚙ Posts from social medias about Mechanical Engineering
            
            Hope you'll enjoy your visit here!
            """
)

