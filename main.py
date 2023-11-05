#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import json

# Define the structure for leisure activities
activities = []


# Initialize the main window
def init_main_window():
    root = tk.Tk()
    root.title("Leisure Time Tracker")

    # Top section for the header
    header_frame = tk.Frame(root)
    header_frame.pack(pady=10)
    tk.Label(header_frame, text="Welcome to Leisure Time Tracker").pack()

    # Middle section for recent activities and calendar/recommendations
    middle_frame = tk.Frame(root)
    middle_frame.pack(pady=10)

    # Frame for recent activities list
    recent_activities_frame = tk.Frame(middle_frame)
    recent_activities_frame.pack(side=tk.LEFT, padx=10)
    tk.Label(recent_activities_frame, text="Recent Activities").pack()
    # ... (Listbox or other widgets for recent activities)

    # Create a scrollbar
    scrollbar = tk.Scrollbar(recent_activities_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a Listbox and attach the scrollbar
    listbox = tk.Listbox(recent_activities_frame, yscrollcommand=scrollbar.set)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Configure the scrollbar
    scrollbar.config(command=listbox.yview)

    # Function to populate the Listbox with recent activities
    def populate_listbox():
        # Clear the Listbox
        listbox.delete(0, tk.END)

        # Sort activities by date, assuming 'date' is in 'YYYY-MM-DD' format
        sorted_activities = sorted(activities, key=lambda x: x["date"], reverse=True)

        # Insert the last 10 activities or all if less than 10
        for activity in sorted_activities[:10]:
            listbox.insert(
                tk.END,
                f"{activity['date']}: {activity['type']} from {activity['start']} to {activity['end']} (Rating: {activity['rating']})",
            )

    # Call the function to populate the Listbox
    populate_listbox()

    # Frame for calendar or recommendations
    calendar_frame = tk.Frame(middle_frame)
    calendar_frame.pack(side=tk.RIGHT, padx=10)
    tk.Label(calendar_frame, text="Your Calendar").pack()
    # ... (Calendar widget or recommendations list)

    cal = Calendar(calendar_frame, selectmode="day", year=2023, month=11, day=5)
    cal.pack(pady=20, padx=20, fill="both", expand=True)

    # Function to display selected date or activities
    def show_date(event):
        selected_date = cal.get_date()
        # You can add functionality to show activities for the selected date
        print(f"Selected Date is: {selected_date}")

    # Bind the calendar event to show_date function
    cal.bind("<<CalendarSelected>>", show_date)

    # Bottom section for action buttons
    action_frame = tk.Frame(root)
    action_frame.pack(pady=10)
    tk.Button(action_frame, text="Add New Activity", command=add_activity_form).pack(
        side=tk.LEFT
    )
    tk.Button(action_frame, text="View Full Log", command=view_full_log).pack(
        side=tk.LEFT
    )
    tk.Button(action_frame, text="Get Recommendation", command=get_recommendation).pack(
        side=tk.LEFT
    )

    return root


def get_recommendation():
    if not activities:
        messagebox.showinfo(
            "Recommendation", "No activities found to base the recommendation on."
        )
        return

    # Calculate the average rating for each activity type
    ratings = {}
    for activity in activities:
        if activity["type"] not in ratings:
            ratings[activity["type"]] = {"total_rating": 0, "count": 0}
        ratings[activity["type"]]["total_rating"] += int(activity["rating"])
        ratings[activity["type"]]["count"] += 1

    # Find the activity type with the highest average rating
    highest_avg_rating = 0
    recommended_activity = None
    for activity_type, rating_info in ratings.items():
        avg_rating = rating_info["total_rating"] / rating_info["count"]
        if avg_rating > highest_avg_rating:
            highest_avg_rating = avg_rating
            recommended_activity = activity_type

    # Display the recommendation
    messagebox.showinfo(
        "Recommendation", f"We recommend you to enjoy some more {recommended_activity}!"
    )


def view_full_log():
    # Create a new top-level window
    log_window = tk.Toplevel()
    log_window.title("Full Activity Log")

    # Create a scrollbar
    scrollbar = tk.Scrollbar(log_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a Listbox and attach the scrollbar
    log_listbox = tk.Listbox(log_window, yscrollcommand=scrollbar.set)
    for activity in activities:
        # Format the string as you like
        log_listbox.insert(
            tk.END,
            f"{activity['date']}: {activity['type']} from {activity['start']} to {activity['end']} with rating {activity['rating']}",
        )
    log_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Configure the scrollbar
    scrollbar.config(command=log_listbox.yview)


def add_activity_form():
    # Create a new top-level window
    add_window = tk.Toplevel()
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

    tk.Label(add_window, text="Date").grid(row=4, column=0)
    date_entry = tk.Entry(add_window)
    date_entry.grid(row=4, column=1)

    tk.Label(add_window, text="Rating").grid(row=3, column=0)
    rating_entry = tk.Entry(add_window)
    rating_entry.grid(row=3, column=1)

    # Function to handle the addition of a new activity
    def add_activity():
        # Here you would gather the data from the entry fields and process it
        activity_type = type_entry.get()
        start_time = start_entry.get()
        end_time = end_entry.get()
        date = date_entry.get()
        rating = rating_entry.get()
        # Validate the inputs here
        activities.append(
            {
                "type": activity_type,
                "start": start_time,
                "end": end_time,
                "date": date,
                "rating": rating,
            }
        )
        # You would also call your save_activities function here
        messagebox.showinfo(
            "Activity Added",
            f"Added {activity_type} from {start_time} to {end_time} with rating {rating}",
        )
        add_window.destroy()  # Close the add activity window

    # Button to submit the new activity
    submit_button = tk.Button(add_window, text="Add Activity", command=add_activity)
    submit_button.grid(row=4, column=0, columnspan=2)


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
