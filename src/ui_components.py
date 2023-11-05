import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar


def create_header_frame(root):
    """
    Creates the header frame with the application title.

    Parameters:
        root (tk.Tk): The root window of the application.

    Returns:
        tk.Frame: The header frame containing the title label.
    """
    header_frame = tk.Frame(root)
    header_frame.pack(pady=10)
    tk.Label(header_frame, text="Welcome to Leisure Time Tracker").pack()
    return header_frame


def create_recent_activities_frame(root, activities):
    """
    Creates a frame that lists recent activities.

    Parameters:
        root (tk.Tk): The root window of the application.
        activities (list): A list of activity dictionaries.

    Returns:
        tk.Frame: The recent activities frame containing the activities list.
    """
    recent_activities_frame = tk.Frame(root)
    recent_activities_frame.pack(
        side=tk.LEFT, padx=10, pady=10, fill="both", expand=True
    )
    tk.Label(recent_activities_frame, text="Recent Activities").pack()

    # Add a scrollbar
    scrollbar = tk.Scrollbar(recent_activities_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Add a listbox to display activities
    listbox = tk.Listbox(recent_activities_frame, yscrollcommand=scrollbar.set)
    for activity in activities:
        listbox.insert(tk.END, f"{activity['date']} - {activity['type']}")
    listbox.pack(side=tk.LEFT, fill="both", expand=True)

    # Configure the scrollbar
    scrollbar.config(command=listbox.yview)

    return recent_activities_frame


def create_calendar_frame(root):
    """
    Creates a frame that contains a calendar widget.

    Parameters:
        root (tk.Tk): The root window of the application.

    Returns:
        tk.Frame: The calendar frame containing the calendar widget.
    """
    calendar_frame = tk.Frame(root)
    calendar_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill="both", expand=True)
    tk.Label(calendar_frame, text="Your Calendar").pack()

    # Create a Calendar widget and pack it
    cal = Calendar(calendar_frame, selectmode="day")
    cal.pack(pady=20)

    return calendar_frame


def create_action_frame(
    root, add_activity_callback, view_log_callback, get_recommendation_callback
):
    """
    Creates a frame with buttons for user actions.

    Parameters:
        root (tk.Tk): The root window of the application.
        add_activity_callback (function): Function to call when adding an activity.
        view_log_callback (function): Function to call when viewing the log.
        get_recommendation_callback (function): Function to call to get recommendations.

    Returns:
        tk.Frame: The action frame containing the action buttons.
    """
    action_frame = tk.Frame(root)
    action_frame.pack(side=tk.BOTTOM, pady=10)

    # Add activity button
    add_activity_btn = tk.Button(
        action_frame, text="Add Activity", command=add_activity_callback
    )
    add_activity_btn.pack(side=tk.LEFT, padx=5)

    # View log button
    view_log_btn = tk.Button(action_frame, text="View Log", command=view_log_callback)
    view_log_btn.pack(side=tk.LEFT, padx=5)

    # Get recommendation button
    get_recommendation_btn = tk.Button(
        action_frame, text="Get Recommendation", command=get_recommendation_callback
    )
    get_recommendation_btn.pack(side=tk.LEFT, padx=5)

    return action_frame


def create_add_activity_form(root, submit_callback):
    """
    Creates a form for adding a new activity.

    Parameters:
        root (tk.Tk): The root window of the application.
        submit_callback (function): The callback function to execute when the form is submitted.

    Returns:
        tk.Toplevel: The top-level window containing the add activity form.
    """
    # Create a new top-level window
    add_activity_window = tk.Toplevel(root)
    add_activity_window.title("Add New Activity")

    # Define labels and entry widgets for the form fields
    tk.Label(add_activity_window, text="Activity Type").grid(row=0, column=0)
    activity_type_entry = tk.Entry(add_activity_window)
    activity_type_entry.grid(row=0, column=1)

    tk.Label(add_activity_window, text="Start Time").grid(row=1, column=0)
    start_time_entry = tk.Entry(add_activity_window)
    start_time_entry.grid(row=1, column=1)

    tk.Label(add_activity_window, text="End Time").grid(row=2, column=0)
    end_time_entry = tk.Entry(add_activity_window)
    end_time_entry.grid(row=2, column=1)

    tk.Label(add_activity_window, text="Date").grid(row=3, column=0)
    date_entry = tk.Entry(add_activity_window)
    date_entry.grid(row=3, column=1)

    tk.Label(add_activity_window, text="Rating").grid(row=4, column=0)
    rating_entry = tk.Entry(add_activity_window)
    rating_entry.grid(row=4, column=1)

    # Define the submit button and its action
    submit_button = tk.Button(
        add_activity_window,
        text="Submit",
        command=lambda: submit_callback(
            activity_type_entry.get(),
            start_time_entry.get(),
            end_time_entry.get(),
            date_entry.get(),
            rating_entry.get(),
        ),
    )
    submit_button.grid(row=5, column=0, columnspan=2)

    return add_activity_window


def create_full_log_view(root, activities):
    """
    Creates a window that displays a full log of activities.

    Parameters:
        root (tk.Tk): The root window of the application.
        activities (list): A list of activity dictionaries.

    Returns:
        tk.Toplevel: The top-level window containing the full log view.
    """
    # Create a new top-level window
    log_window = tk.Toplevel(root)
    log_window.title("Activity Log")

    # Add a scrollbar
    scrollbar = tk.Scrollbar(log_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a listbox to display the activities
    listbox = tk.Listbox(log_window, yscrollcommand=scrollbar.set)
    for activity in activities:
        # Format the activity details into a string for the listbox
        activity_details = f"{activity['date']} - {activity['type']}: {activity['start']} to {activity['end']}, Rating: {activity['rating']}"
        listbox.insert(tk.END, activity_details)
    listbox.pack(side=tk.LEFT, fill="both", expand=True)

    # Configure the scrollbar
    scrollbar.config(command=listbox.yview)

    return log_window
