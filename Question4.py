# File: functions_task.py
from math import pi

def area_of_circle(radius):
    # Validate radius
    if radius <= 0:
        return "Error: Radius must be greater than 0."
    # Calculate area and round to 2 decimal places
    area = pi * radius ** 2
    return round(area, 2)