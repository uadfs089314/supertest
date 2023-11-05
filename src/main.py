import tkinter as tk

# Our own imports
from ui_components import (
    create_header_frame,
    create_recent_activities_frame,
    create_calendar_frame,
    create_action_frame,
    create_add_activity_form,
    create_full_log_view,
)
from data_management import add_activity, get_recent_activities

# This is your main application data structure for activities
activities = []


# Callback functions for user actions
def add_activity_callback():
    def submit_activity(type, start, end, date, rating):
        # Here you would include validation and possibly conversion (e.g., rating to int)
        activity = {
            "type": type,
            "start": start,
            "end": end,
            "date": date,
            "rating": int(rating),
        }
        add_activity(activity)
        # Close the add activity window after submission
        add_activity_window.destroy()
        # Refresh the recent activities list or other UI components as needed

    # Open the add activity form
    add_activity_window = create_add_activity_form(root, submit_activity)


def view_log_callback():
    # Open the full log view window
    activities = get_recent_activities()
    create_full_log_view(root, activities)


def get_recommendation_callback():
    # This is a placeholder for the recommendation logic
    print("This will show activity recommendations.")


# Initialize the main application window
root = tk.Tk()
root.title("Leisure Time Tracker")

# Create and pack the UI components from ui_components.py
header_frame = create_header_frame(root)
recent_activities_frame = create_recent_activities_frame(root)
calendar_frame = create_calendar_frame(root)
action_frame = create_action_frame(
    root, add_activity_callback, view_log_callback, get_recommendation_callback
)

# Start the Tkinter event loop
root.mainloop()
