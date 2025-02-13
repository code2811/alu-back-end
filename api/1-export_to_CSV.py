#!/usr/bin/python3
"""
Script to export employee task data to CSV format
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Export employee tasks to CSV file"""
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

    # Write to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        # Write each task as a row in the CSV
        for todo in todos:
            writer.writerow([
                str(employee_id),
                username,
                str(todo.get('completed')),
                todo.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1);
