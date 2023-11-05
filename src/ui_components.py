import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar


# Function to create the header frame
def create_header_frame(root):
    header_frame = tk.Frame(root)
    header_frame.pack(pady=10)
    tk.Label(header_frame, text="Welcome to Leisure Time Tracker").pack()
    return header_frame


# Function to create the recent activities frame
def create_recent_activities_frame(root):
    recent_activities_frame = tk.Frame(root)
    recent_activities_frame.pack(
        side=tk.LEFT, padx=10, pady=10, fill="both", expand=True
    )
    tk.Label(recent_activities_frame, text="Recent Activities").pack()
    # Listbox or other widgets for recent activities will be added here
    return recent_activities_frame


# Function to create the calendar frame
def create_calendar_frame(root):
    calendar_frame = tk.Frame(root)
    calendar_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill="both", expand=True)
    tk.Label(calendar_frame, text="Your Calendar").pack()
    # Calendar widget or recommendations list will be added here
    return calendar_frame


# Function to create the action buttons frame
def create_action_frame(
    root, add_activity_callback, view_log_callback, get_recommendation_callback
):
    action_frame = tk.Frame(root)
    action_frame.pack(pady=10)
    tk.Button(
        action_frame, text="Add New Activity", command=add_activity_callback
    ).pack(side=tk.LEFT)
    tk.Button(action_frame, text="View Full Log", command=view_log_callback).pack(
        side=tk.LEFT
    )
    tk.Button(
        action_frame, text="Get Recommendation", command=get_recommendation_callback
    ).pack(side=tk.LEFT)
    return action_frame


# Function to create the add activity form
def create_add_activity_form(root, submit_callback):
    add_window = tk.Toplevel(root)
    add_window.title("Add New Activity")

    # Define the labels and entry widgets for the activity form
    tk.Label(add_window, text="Activity Type").grid(row=0, column=0)
    type_entry = tk.Entry(add_window)
    type_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Start Time").grid(row=1, column=0)
    start_entry = tk.Entry(add_window)
    start_entry.grid(row=1, column=1)

    tk.Label(add_window, text="End Time").grid(row=2, column=0)
    end_entry = tk.Entry(add_window)
    end_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Date").grid(row=3, column=0)
    date_entry = tk.Entry(add_window)
    date_entry.grid(row=3, column=1)

    tk.Label(add_window, text="Rating").grid(row=4, column=0)
    rating_entry = tk.Entry(add_window)
    rating_entry.grid(row=4, column=1)

    # Button to submit the new activity
    submit_button = tk.Button(
        add_window,
        text="Add Activity",
        command=lambda: submit_callback(
            type_entry.get(),
            start_entry.get(),
            end_entry.get(),
            date_entry.get(),
            rating_entry.get(),
        ),
    )
    submit_button.grid(row=5, column=0, columnspan=2)

    return add_window


# Function to create the full log view
def create_full_log_view(root, activities):
    log_window = tk.Toplevel(root)
    log_window.title("Full Activity Log")

    # Create a scrollbar
    scrollbar = tk.Scrollbar(log_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a Listbox and attach the scrollbar
    log_listbox = tk.Listbox(log_window, yscrollcommand=scrollbar.set)
    for activity in activities:
        log_listbox.insert(
            tk.END,
            f"{activity['date']}: {activity['type']} from {activity['start']} to {activity['end']} with rating {activity['rating']}",
        )
    log_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Configure the scrollbar
    scrollbar.config(command=log_listbox.yview)

    return log_window
