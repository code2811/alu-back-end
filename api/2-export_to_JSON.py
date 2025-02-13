#!/usr/bin/python3
"""
Script to export employee task data to JSON format
"""
import json
import requests
import sys


def export_to_json(employee_id):
    """Export employee tasks to JSON file"""
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found")
        sys.exit(1)

    user = user_response.json()
    username = user.get('username')

    # Get tasks for the employee
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    if todos_response.status_code != 200:
        print(f"Could not fetch tasks for employee {employee_id}")
        sys.exit(1)

    todos = todos_response.json()

    # Format tasks according to requirements
    tasks_list = [
        {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        for todo in todos
    ]

    # Create JSON object with required format
    json_data = {str(employee_id): tasks_list}

    # Write to file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

