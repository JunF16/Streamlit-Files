import streamlit as st

# Page setup
about_page = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\1_About me.py",
    title="About Me",
    default=True,
)
project_1_page = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\2_My Projects.py",
    title="My Projects",
)
project_2_page = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\3_Contact.py",
    title="Contact",
)

# Navigation setup without sections
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# Navigation setup with sections
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# Shared assets
st.logo(r"C:\Users\Acer\Streamlit Files\assets\gear.png")
st.sidebar.text("Made by yours truly ❤ ")

# Run navigation
pg.run()