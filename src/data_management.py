import json
from pathlib import Path

# Define the path to the JSON file where activities will be stored
DATA_FILE = Path(__file__).parent.parent / "activities.json"


def load_activities():
    """
    Load activities from a JSON file.
    If the file doesn't exist, return an empty list.
    """
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_activities(activities):
    """
    Save activities to a JSON file.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(activities, file, indent=4)


def add_activity(activity_data):
    """
    Add a new activity to the list and save it to the file.
    """
    activities = load_activities()
    activities.append(activity_data)
    save_activities(activities)


def get_recent_activities(limit=10):
    """
    Get the most recent activities, limited to the specified number.
    """
    activities = load_activities()
    # Sort activities by date, assuming 'date' is in 'YYYY-MM-DD' format
    sorted_activities = sorted(activities, key=lambda x: x["date"], reverse=True)
    return sorted_activities[:limit]


# Additional functions for processing activities can be added here
