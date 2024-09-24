import streamlit as st

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
