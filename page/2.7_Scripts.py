import streamlit as st
import matplotlib.pyplot as plt
from th_scripts.random_story_generator import generate_story
from th_scripts.convert_wind_speed import convert_wind_speed_to_kph 
from th_scripts.pdrop_darcy_weisbach import calculate_pressure_drop
from th_scripts.mean_calculator import calculate_mean
from th_scripts.extrapolation import linear_extrapolate_y, linear_extrapolate_x

st.title("Linear Extrapolation Tool")

mode = st.radio("What do you want to find?", ["Find y from x", "Find x from y"])

x_input = st.text_input("Example x values (comma-separated)", "1,2,3,4")
y_input = st.text_input("Example y values (comma-separated)", "2,4,6,8")

try:
    x_values = [float(x.strip()) for x in x_input.split(",")]
    y_values = [float(y.strip()) for y in y_input.split(",")]

    if len(x_values) < 2 or len(y_values) < 2 or len(x_values) != len(y_values):
        st.error("Please enter at least two matching x and y values.")
    else:
        result = None  # Initialize result
        extrapolated_point = None  # Store the point to plot
        target_x = 0.0
        target_y = 0.0
        
        if mode == "Find y from x":
            target_x = st.number_input("Enter target x value", value=6.0)
            if st.button("Extrapolate y"):
                result = linear_extrapolate_y(x_values, y_values, target_x)
                extrapolated_point = (target_x, result)  # Store as (x, y)
                st.success(f"At x = {target_x}, extrapolated y = {result}")
        else:
            target_y = st.number_input("Enter target y value", value=12.0)
            if st.button("Extrapolate x"):
                result = linear_extrapolate_x(x_values, y_values, target_y)
                extrapolated_point = (result, target_y)  # Store as (x, y)
                st.success(f"At y = {target_y}, extrapolated x = {result}")

        # Plotting - only show extrapolated point if calculation was done
        fig, ax = plt.subplots()
        ax.plot(x_values, y_values, 'bo-', label="Known Data")
        
        # Only plot extrapolated point if we have one
        if extrapolated_point is not None:
            ax.plot(extrapolated_point[0], extrapolated_point[1], 'ro', 
                   label="Extrapolated Point", markersize=8)
            
            # Add reference lines based on mode
            if mode == "Find y from x":
                ax.axvline(x=target_x, color='r', linestyle='--', 
                          linewidth=0.5, alpha=0.7)
            else:
                ax.axhline(y=target_y, color='r', linestyle='--', 
                          linewidth=0.5, alpha=0.7)

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Linear Extrapolation")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)

        st.pyplot(fig)

except Exception as e:
    st.error(f"Error: {e}")

st.markdown("---")

st.title("Mean Calculator")

# Input from the user
user_input = st.text_input("Enter numbers separated by commas:")

if st.button("Calculate Mean"):
    try:
        # Process the input into a list of integers
        numbers = [int(num.strip()) for num in user_input.split(",")]

        # Calculate the mean
        mean = calculate_mean(numbers)

        # Display the result
        if mean is not None:
            st.success(f"The mean of the entered numbers is: {mean}")
        else:
            st.warning("No valid numbers entered. Please try again.")
    except ValueError:
        st.error("Invalid input. Please enter only numbers separated by commas.")

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
        st.write(f"Calculated Pressure Drop: {pressure_drop:,.2f} Pa")
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
