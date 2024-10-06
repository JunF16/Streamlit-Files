from PIL import Image
import streamlit as st

# Load Assets
img_Cert_1 = Image.open("images/Solidworks/Ex 223.png")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("Solidworks Practice 1")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("Solidworks 3D model")
    st.write(
        """
         Solidworks practice from (Insert author)
        """
        )
    st.markdown("[Learn from here...](Insert link here)")