from PIL import Image
import streamlit as st
from pathlib import Path

# Load Assets
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
img_Cert_1 = Image.open("images/Revit/2 Storey House.PNG")
img_Cert_2 = Image.open("images/Revit/S15 Revit.PNG")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("Revit Practice 2")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_2)
with text_column:
    st.subheader("Studio Bungalow")
    st.write(
        """
        Revit MEP Practice from S15 Studio
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=Oyj1CL74svY&list=PL6ZitbPhhYsTOhWF0aawbcdXJV589TQFL&index=10)")

with st.container():
    st.write("---")
    st.header("Revit Practice 1")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("2 Storey House")
    st.write(
        """
        Revit MEP Practice from Renato Roxas Jr.
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/watch?v=YCfAYsVAFug&list=PL6ZitbPhhYsTOhWF0aawbcdXJV589TQFL&index=6)")