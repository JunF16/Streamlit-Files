import streamlit as st

st.title("About me")

# Header Section
st.subheader("Hello, I am John Mark Casuga.")
st.subheader("A Registered Mechanical Engineer from the Philippines")
st.write("This is a web page dedicated to showcase my passion in all things related to Mechanical Engineering.")
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
      