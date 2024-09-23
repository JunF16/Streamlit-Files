import requests
import streamlit as st
from streamlit_option_menu import option_menu

# 1 as sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Contact"],
        default_index=0,
        orientation="horizontal",
    )

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected =="Contact":
    st.title(f"You have selected {selected}")

#Page Setup
about_page = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\Homepage.py",
    title="About me",
    default=True,
)
My_Projects = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\2_My Projects.py",
    title="My Projects",
)
Contact = st.Page(
    page=r"C:\Users\Acer\Streamlit Files\3_Contact.py",
    title="Contact",
)

# Navigation setup
pg = st.navigation(pages=[My_Projects, Contact])

# Run navigation
pg.run()

#Load Assets

# Use Local CSS, this function takes a file name as an argument w/a html style
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css(r"C:\Users\Acer\Streamlit Files\styles\style.css")

# Header Section
st.subheader("Hello, I am John Mark Casuga.")
st.title("A Registered Mechanical Engineer from the Philippines")
st.write("A web page dedicated to showcase my passion in all things related to Mechanical Engineering.")
st.write("[Learn more about me >](https://ph.linkedin.com/in/john-mark-casuga-rmee)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What to expect on my web page")
        st.write("##")
        st.write(
            """
            I created this web page to share my progress in learning various tools in 2D and 3D CAD modelling software such as Solidworks, Revit and Autodesk. 
            I also post practice files I found interesting on Youtube which may include tutorials on various softwares.
            
            What you'll see on this web page:

               -My 2D and 3D renders from Solidworks, Revit and AutoCAD

               -Various practice files I found from Youtube

               -Posts from social medias about Mechanical Engineering
            
            Hope you'll enjoy your visit here!
            """
        )
        
# Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
        # insert image
     with text_column:
        st.subheader("1st Project Placeholder")
        st.write(
            """
            Project description
            """
        )
        st.markdown("[Learn from here...](Insert link here)")

# Contact form
with st.container():
    st.write("---")
    st.header("Got any suggestions?")
    st.write("##")

# Documentation: https://formsubmit.co/ !Change email address!, set captcha to True later(removed)
contact_form = """
<form method="POST" action="https://formsubmit.co/junfontanos16@gmail.com">
    <input type="text" name="name" placeholder="Your name(optional)" required>
    <input type="email" name="email" placeholder="Your email(optional)" required>
    <textarea name="message" placeholder="Your message here(optional)" required></textarea>
    <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()




