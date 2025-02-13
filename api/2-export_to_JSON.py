#!/usr/bin/python3
"""
This script fetches the TODO list progress of an employee using an API, and
exports the data to a JSON file in the format:
{
    "USER_ID": [
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
        ...
    ]
}
The file name is generated based on the USER_ID.
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """
    Retrieves the TODO list and employee details from the API and 
    exports the task data to a JSON file.

    Args:
        employee_id (int): The ID of the employee to fetch the TODO list for.
    """
    # API URL for the user's TODO data
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    # Make a GET request to the API to fetch TODO list
    response = requests.get(url)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        todos = response.json()
        
        # Get the employee name by fetching user info
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)
        if user_response.status_code == 200:
            user_info = user_response.json()
            username = user_info['username']
        else:
            print("Failed to retrieve employee details.")
            return
        
        # Create the JSON file name based on the employee ID
        file_name = f"{employee_id}.json"
        
        # Prepare the data to be written to the JSON file
        data = {employee_id: []}
        
        for task in todos:
            task_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            }
            data[employee_id].append(task_data)
        
        # Write the data to the JSON file
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Data has been exported to {file_name}")
    else:
        print("Failed to retrieve TODO list.")


if __name__ == "__main__":
    """
    Main function to handle command-line argument and call the function 
    to export the employee TODO list to JSON.
    """
    # Check if employee ID was passed as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command-line arguments
    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Please provide a valid integer for employee ID.")

