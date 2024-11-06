import streamlit as st
from PIL import Image
from pathlib import Path

# Load Assets
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
img_Cert_1 = Image.open("images/Certs/REVIT MEP.PNG")
img_Cert_2 = Image.open("images/Certs/AutoCAD.PNG")
img_Cert_3 = Image.open("images/Certs/M365F.PNG")
img_Cert_4 = Image.open("images/Certs/GPM.PNG")
img_Cert_5 = Image.open("images/Certs/COSH.PNG")
img_Cert_6 = Image.open("images/Certs/BOSH.PNG")
img_Cert_7 = Image.open("images/Certs/COC_ConsEst.PNG")
img_Cert_8 = Image.open("images/Certs/COC_SnH.PNG")
img_Cert_9 = Image.open("images/Certs/COC_Read.PNG")
img_Cert_10 = Image.open("images/Certs/COC_PnS.PNG")

# Projects
with st.container():
    st.write("---")
    st.header("Certificate #10")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("Construction Management: Planning and Scheduling")
    st.write(
            """
            Date Finished: 29 October 2024
            """
        )
    st.markdown("[Learn from here...](https://www.linkedin.com/learning/construction-management-planning-and-scheduling)")

with st.container():
    st.write("---")
    st.header("Certificate #9")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_9)
with text_column:
    st.subheader("Construction Management: Reading Civil Construction Drawings")
    st.write(
            """
            Date Finished: 22 October 2024
            """
        )
    st.markdown("[Learn from here...](https://www.linkedin.com/learning/construction-management-reading-civil-construction-drawings/start-your-construction-project-right)")

with st.container():
    st.write("---")
    st.header("Certificate #8")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_8)
with text_column:
    st.subheader("Construction Management: Safety and Health")
    st.write(
            """
            Date Finished: 16 October 2024
            """
        )
    st.markdown("[Learn from here...](https://www.linkedin.com/learning/construction-management-safety-and-health/safety-is-everyone-s-job)")

with st.container():
    st.write("---")
    st.header("Certificate #7")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_7)
with text_column:
    st.subheader("Construction Estimating")
    st.write(
            """
            Date Finished: 08 October 2024
            """
        )
    st.markdown("[Learn from here...](https://www.linkedin.com/learning/learning-construction-estimating-17283903/learn-construction-estimating-the-right-way)")

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