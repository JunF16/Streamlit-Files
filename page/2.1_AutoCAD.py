from PIL import Image
import streamlit as st
from pathlib import Path

# Load Assets
current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
img_Cert_1 = Image.open("images/AutoCAD images/SourceCAD AutoCAD 2D 1.PNG")
img_Cert_2 = Image.open("images/AutoCAD images/SourceCAD AutoCAD 3D 1.PNG")

# Projects (add above succeeding project)
with st.container():
    st.write("---")
    st.header("AutoCAD practice 2")
    st.write("##")
    image_column, text_column = st.columns((2,2))
    
with image_column:
    st.image(img_Cert_2)
with text_column:
    st.subheader("AutoCAD 3D")
    st.write(
        """
         AutoCAD practice from SourceCAD
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/playlist?list=PLcH1MIEuSvoH55AygdATks6ZX6dYO2kzA)")

with st.container():
    st.write("---")
    st.header("AutoCAD practice 1")
    st.write("##")
    image_column, text_column = st.columns((2,2))
    
with image_column:
    st.image(img_Cert_1)
with text_column:
    st.subheader("AutoCAD 2D")
    st.write(
        """
         AutoCAD practice from SourceCAD
        """
        )
    st.markdown("[Learn from here...](https://www.youtube.com/playlist?list=PLcH1MIEuSvoGT7bY9_W1QseB8gxsyZSJP)")
