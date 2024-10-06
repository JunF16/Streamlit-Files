from PIL import Image
import streamlit as st

# Load Assets
img_Cert_1 = Image.open(r"C:\Users\Acer\Streamlit Files\images")

# Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("1st Project Placeholder")
    st.write(
        """
         Project description
        """
        )
    st.markdown("[Learn from here...](Insert link here)")
