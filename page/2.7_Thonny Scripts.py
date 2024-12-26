import streamlit as st
import matplotlib.pyplot as plt
from th_scripts.random_story_generator import generate_story
from th_scripts.convert_wind_speed import convert_wind_speed_to_kph 
from th_scripts.pdrop_darcy_weisbach import calculate_pressure_drop

st.title("Dynamic Plot Chart")

# User input for data points
num_points = st.number_input("Number of data points:", min_value=1, step=1)
x_values = []
y_values = []

for i in range(num_points):
    x = st.number_input(f"X value {i+1}:", key=f"x{i}")
    y = st.number_input(f"Y value {i+1}:", key=f"y{i}")
    x_values.append(x)
    y_values.append(y)

if st.button("Generate Plot"):
    # Generate plot using Matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.title("User Input Plot")
    plt.grid(True)

    st.pyplot(plt)

st.markdown("---")

st.title("Pressure Drop using Darcy-Weisbach Equation")

# Text fields for each parameter
friction_factor = st.number_input("Friction Factor:", min_value=0.0, step=0.01, format="%.2f")
length = st.number_input("Length of pipe (meters):", min_value=0.0, step=1.0, format="%.2f")
diameter = st.number_input("Diameter of pipe (meters):", min_value=0.0, step=0.01, format="%.2f")
density = st.number_input("Density of liquid (kg/m³):", min_value=0.0, step=1.0, format="%.2f")
velocity = st.number_input("Velocity of flow (m/s):", min_value=0.0, step=0.1, format="%.2f")
  
if st.button("Calculate Pressure Drop"):
    try:
        # Call the function to calculate pressure drop
        pressure_drop = calculate_pressure_drop(friction_factor, length, diameter, density, velocity)
        # Display the result
        st.write(f"Calculated Pressure Drop: {pressure_drop:.2f} Pa")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown("---")

st.title("Wind Speed Converter") 
st.write("Enter a wind speed in meters per second (m/s) to convert to kilometers per hour (kph):") 

# User input for wind speed 
user_speed_mps = st.number_input("Wind Speed (m/s)", min_value=0.0, step=0.1, format="%.2f") 

# Initialize user_speed_kph 
user_speed_kph = None 

if st.button("Convert"): 
    user_speed_kph = convert_wind_speed_to_kph(user_speed_mps) 
    st.write(f"Wind speed in kilometers per hour (kph): {user_speed_kph:.2f}") 

# Break between scripts 
st.markdown("---")

# Thonny script 1
st.title("Random Story Generator")

if st.button("Generate Story"):
    # Call the function from Thonny script 1
    story = generate_story()
    # Display the story
    st.write("Here's your randomly generated story:")
    st.write(story)
