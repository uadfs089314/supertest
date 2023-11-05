#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import json

# Define the structure for leisure activities
activities = []


# Initialize the main window
def init_main_window():
    root = tk.Tk()
    root.title("Leisure Time Tracker")

    # Frame for adding activities
    add_activity_frame = tk.Frame(root)
    add_activity_frame.pack(pady=10)

    tk.Label(add_activity_frame, text="Activity Type").grid(row=0, column=0)
    type_entry = tk.Entry(add_activity_frame)
    type_entry.grid(row=0, column=1)

    tk.Label(add_activity_frame, text="Start Time").grid(row=1, column=0)
    start_entry = tk.Entry(add_activity_frame)
    start_entry.grid(row=1, column=1)

    tk.Label(add_activity_frame, text="End Time").grid(row=2, column=0)
    end_entry = tk.Entry(add_activity_frame)
    end_entry.grid(row=2, column=1)

    tk.Label(add_activity_frame, text="Rating").grid(row=3, column=0)
    rating_entry = tk.Entry(add_activity_frame)
    rating_entry.grid(row=3, column=1)

    add_button = tk.Button(
        add_activity_frame,
        text="Add Activity",
        command=lambda: add_activity(type_entry, start_entry, end_entry, rating_entry),
    )
    add_button.grid(row=4, column=0, columnspan=2)

    # Add more components to the main window here

    return root


# Function to add a new leisure activity
def add_activity(type_entry, start_entry, end_entry, rating_entry):
    activity_type = type_entry.get()
    start_time = start_entry.get()
    end_time = end_entry.get()
    rating = rating_entry.get()
    # Validate the inputs here
    activities.append(
        {"type": activity_type, "start": start_time, "end": end_time, "rating": rating}
    )
    save_activities()
    messagebox.showinfo(
        "Activity Added",
        f"Added {activity_type} from {start_time} to {end_time} with rating {rating}",
    )


# Function to save activities to a file
def save_activities():
    with open("activities.json", "w") as f:
        json.dump(activities, f)


# Function to load activities from a file
def load_activities():
    try:
        with open("activities.json", "r") as f:
            global activities
            activities = json.load(f)
    except FileNotFoundError:
        activities = []


# Start the GUI application
if __name__ == "__main__":
    load_activities()
    main_window = init_main_window()
    main_window.mainloop()
