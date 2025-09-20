def linear_extrapolate(x_values, y_values, target_x):
    if len(x_values) < 2 or len(y_values) < 2:
        raise ValueError("Need at least two data points for extrapolation.")
    if len(x_values) != len(y_values):
        raise ValueError("x and y lists must be the same length.")

    # Use the last two points for extrapolation
    x1, x2 = x_values[-2], x_values[-1]
    y1, y2 = y_values[-2], y_values[-1]

    # Calculate slope (m) and intercept (b)
    m = (y2 - y1) / (x2 - x1)
    b = y2 - m * x2

    # Extrapolate
    extrapolated_y = m * target_x + b
    return extrapolated_y

# Example usage
x_data = [1, 2, 3, 4]
y_data = [2, 4, 6, 8]
target = 6

result = linear_extrapolate(x_data, y_data, target)
print(f"Extrapolated value at x = {target} is y = {result}")