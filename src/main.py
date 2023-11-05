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
    """
    Callback for adding a new activity.
    Opens a form for the user to enter activity details and submit.
    """

    def submit_activity(type, start, end, date, rating):
        """
        Submits a new activity to the activity log.

        Parameters:
            type (str): The type of the activity.
            start (str): The start time of the activity.
            end (str): The end time of the activity.
            date (str): The date of the activity.
            rating (int): The user's rating of the activity.
        """
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
    """
    Callback for viewing the full activity log.
    Opens a window displaying a list of all past activities.
    """
    activities = get_recent_activities()
    create_full_log_view(root, activities)


def get_recommendation_callback():
    """
    Callback for getting activity recommendations.
    This function will be replaced with actual recommendation logic.
    """
    print("This will show activity recommendations.")


# Load activities from the data file
activities = get_recent_activities()

# Initialize the main application window
root = tk.Tk()
root.title("Leisure Time Tracker")

# Create the UI components
header_frame = create_header_frame(root)
middle_section_frame = tk.Frame(root)
middle_section_frame.pack(side=tk.TOP, fill="both", expand=True)
recent_activities_frame = create_recent_activities_frame(
    middle_section_frame, activities
)
calendar_frame = create_calendar_frame(middle_section_frame)
action_frame = create_action_frame(
    root, add_activity_callback, view_log_callback, get_recommendation_callback
)

# Start the Tkinter event loop
root.mainloop()
