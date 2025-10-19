def linear_extrapolate_y(x_values, y_values, target_x):
    x1, x2 = x_values[-2], x_values[-1]
    y1, y2 = y_values[-2], y_values[-1]
    m = (y2 - y1) / (x2 - x1)
    b = y2 - m * x2
    return m * target_x + b

def linear_extrapolate_x(x_values, y_values, target_y):
    x1, x2 = x_values[-2], x_values[-1]
    y1, y2 = y_values[-2], y_values[-1]
    m = (y2 - y1) / (x2 - x1)
    b = y2 - m * x2
    return (target_y - b) / m