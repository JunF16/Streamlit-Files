import streamlit as st
from PIL import Image

# Load Assets
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
img_Cert_1 = Image.open("Streamlit FIles/images/Certs/REVIT MEP.png")
img_Cert_2 = Image.open("Streamlit FIles/images/Certs/AutoCAD.png")
img_Cert_3 = Image.open("Streamlit FIles/images/Certs/M365F.png")
img_Cert_4 = Image.open("Streamlit FIles/images/Certs/GPM.png")
img_Cert_5 = Image.open("Streamlit FIles/images/Certs/COSH.png")
img_Cert_6 = Image.open("Streamlit FIles/images/Certs/BOSH.png")

# Projects
with st.container():
    st.write("---")
    st.header("Certificate #6")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("Revit MEP Essentials For Beginners")
    st.write(
            """
            Date Finished: 18 August 2024
            """
        )
    st.markdown("[Learn from here...](https://sourcecad.com/courses/revit-mep-essentials-for-beginners/)")

with st.container():
    st.write("---")
    st.header("Certificate #5")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_2)
with text_column:
    st.subheader("AutoCAD Essentials Course for Complete Beginners")
    st.write(
        """
         Date Finished: 08 July 2024
        """
        )
    st.markdown("[Learn from here...](https://sourcecad.com/courses/autocad-essentials-course/)")

with st.container():
    st.write("---")
    st.header("Certificate #4")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_3)
with text_column:
    st.subheader("Microsoft 365 Fundamentals")
    st.write(
        """
         Date Finished: 26 April 2024
        """
        )
    st.markdown("[Learn from here...](https://www.coursera.org/specializations/microsoft-365-fundamentals#courses)")

with st.container():
    st.write("---")
    st.header("Certificate #3")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_4)
with text_column:
    st.subheader("Google Project Management")
    st.write(
        """
         Date Finished: 18 April 2024
        """
        )
    st.markdown("[Learn from here...](https://www.coursera.org/professional-certificates/google-project-management#courses)")

with st.container():
    st.write("---")
    st.header("Certificate #2")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_5)
with text_column:
    st.subheader("Construction Occupational Safety and Health")
    st.write(
        """
         Date Finished: 10 July 2022
        """
        )
    st.markdown("[Learn from here...](https://web.facebook.com/BECMISafety/?_rdc=1&_rdr)")

with st.container():
    st.write("---")
    st.header("Certificate #1")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_6)
with text_column:
    st.subheader("Basic Occupational Safety and Health")
    st.write(
        """
         Date Finished: 26 June 2022
        """
        )
    st.markdown("[Learn from here...](https://web.facebook.com/BECMISafety/?_rdc=1&_rdr)")