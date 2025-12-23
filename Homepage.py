import streamlit as st
from datetime import datetime, timedelta, timezone

# Page setup
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .scroll-x {
        display: flex;
        justify-content: center;   /* centers row content */
        overflow-x: auto;
        gap: 15px;
        padding: 10px 0;
    }
    .scroll-x img {
        max-height: 200px;
        border-radius: 10px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.2);
        transition: transform 0.2s;
    }
    .scroll-x img:hover {
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

project_8_page = st.Page(
    page="page/2.7_Scripts.py",
    title="Scripts"
)
project_9_page = st.Page(
    page="page/2.8_Excel.py",
    title="Excel Web App"
)

# Navigation setup without sections
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# Navigation setup with sections
pg = st.navigation(
    {
        "Projects": [project_9_page, project_8_page],
    }
)

# Combined Date and Time Display (Client-side)
st.components.v1.html("""
<style>
    #clock-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: auto;
        flex-direction: column;
        margin-bottom: -10px;
    }
    #date, #clock {
        font-size: 2em;
        font-weight: bold;
        font-family: Arial, sans-serif;
        color: red;
    }
    #date {
        font-size: 1.2em;
        margin-bottom: 5px; /* Adds space between date and time */
    }
</style>

<div id="clock-container">
    <div id="date"></div>
    <div id="clock"></div>
</div>

<script>
function updateClock() {
    // Create a date object for UTC+8
    const now = new Date(new Date().toLocaleString("en-US", {timeZone: "Asia/Singapore"}));
    const clock = document.getElementById('clock');
    const date = document.getElementById('date');
    const dateOptions = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    date.innerHTML = now.toLocaleDateString('en-US', dateOptions);
    clock.innerHTML = now.toLocaleTimeString();
}
setInterval(updateClock, 1000);
updateClock();
</script>
""", height=80)

st.logo("downloads/gear.png")
st.sidebar.text("Made by yours truly ❤ ")

# Run navigation
pg.run()