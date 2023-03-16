import math
import tkinter as tk

# Define the function to calculate true heading and ground speed
def calculate():
    wind_direction = float(wind_direction_entry.get())
    wind_velocity = float(wind_velocity_entry.get())
    true_air_speed = float(true_air_speed_entry.get())
    track = float(track_entry.get())

    # Convert degrees to radians
    wind_direction_rad = math.radians(wind_direction)
    track_rad = math.radians(track)

    # Calculate angle between track and wind direction
    angle = wind_direction_rad - track_rad

    # Calculate wind correction angle (WCA)
    wca = math.asin((wind_velocity / true_air_speed) * math.sin(angle))

    # Calculate true heading
    true_heading = track_rad + wca

    # Calculate ground speed
    ground_speed = true_air_speed * math.cos(wca) - wind_velocity * math.cos(wind_direction_rad - true_heading)

    # Convert true heading and ground speed back to degrees
    true_heading_deg = math.degrees(true_heading)
    ground_speed_kts = round(ground_speed, 1)

    # Update the labels with the results
    true_heading_label.config(text=f"True heading: {true_heading_deg:.1f} degrees")
    ground_speed_label.config(text=f"Ground speed: {ground_speed_kts} knots")

# Create a GUI window
window = tk.Tk()

# Set the title and dimensions of the window
window.title("How to Calculate Heading and Ground Speed")
window.geometry("800x600")

# Add a title label
title_label = tk.Label(window, text="How To Calculate Heading And Ground Speed", font=("Cray", 26, "bold"))
title_label.pack(side="top", pady=20)

# Create a label for each input field
wind_direction_label = tk.Label(window, text="Wind direction (deg):", font=("Arial", 18))
wind_direction_label.pack()
wind_direction_entry = tk.Entry(window, font=("Arial", 18), bd=2)
wind_direction_entry.pack()

wind_velocity_label = tk.Label(window, text="Wind velocity (knots):", font=("Arial", 18))
wind_velocity_label.pack()
wind_velocity_entry = tk.Entry(window, font=("Arial", 18), bd=2)
wind_velocity_entry.pack()

true_air_speed_label = tk.Label(window, text="True air speed (knots):", font=("Arial", 18))
true_air_speed_label.pack()
true_air_speed_entry = tk.Entry(window, font=("Arial", 18), bd=2)
true_air_speed_entry.pack()

track_label = tk.Label(window, text="Track (deg):", font=("Arial", 18))
track_label.pack()
track_entry = tk.Entry(window, font=("Arial", 18), bd=2)
track_entry.pack()

# Create a button to calculate the results
calculate_button = tk.Button(window, text="Calculate", font=("Arial", 18), command=calculate)
calculate_button.pack()

# Create labels for the results
true_heading_label = tk.Label(window, font=("Arial", 18))
true_heading_label.pack()

ground_speed_label = tk.Label(window, font=("Arial", 18))
ground_speed_label.pack()

# Run the GUI window
window.mainloop()
