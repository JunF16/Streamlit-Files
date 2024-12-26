def calculate_pressure_drop(friction_factor, length, diameter, density, velocity):
    # Applying the Darcy-Weisbach equation
    pressure_drop = friction_factor * (length / diameter) * (density * velocity**2) / 2
    return pressure_drop
