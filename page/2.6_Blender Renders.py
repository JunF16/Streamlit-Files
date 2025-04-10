from PIL import Image
import streamlit as st
from pathlib import Path

# Load Assets
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
img_Cert_1 = Image.open("images/Blender/audi r8 v10 turq.png")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("Blender Render 1")
    st.write("##")
    image_column, text_column = st.columns((2,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("Audi R8 V10 in Turquoise")
    st.write(
        """
         Blender Car Model by Me
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/@NaturalArtFreak)")
