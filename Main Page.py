import streamlit as st
# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# Page setup
about_page = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\1.1_About me.py",
    title="About Me",
    default=True,
)
project_1_page = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\1.2_Certificates.py",
    title="Certificates",
)
project_2_page = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\2.1_AutoCAD.py",
    title="AutoCAD",
)
project_3_page = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\2.2_Revit.py",
    title="Revit"
)
project_4_page = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\2.3_Solidworks.py",
    title="Solidworks",
)
project_5_page = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\2.4_Capstone.py",
    title="Capstone",
)

# Navigation setup without sections
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# Navigation setup with sections
pg = st.navigation(
    {
        "Info": [about_page, project_1_page],
        "Projects": [project_2_page, project_3_page, project_4_page, project_5_page],
    }
)

# Shared assets
st.logo(r"C:\Users\Acer\Streamlit Files\assets\gear.png")
st.sidebar.text("Made by yours truly ❤ ")

# Run navigation
pg.run()