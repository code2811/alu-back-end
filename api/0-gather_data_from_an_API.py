#!/usr/bin/python3
"""
This script fetches TODO list progress of an employee using an API.
It accepts an employee ID as a command-line argument and displays the 
employee's name, the number of completed tasks, and their titles in the
specified format.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieves the TODO list and employee details from the API and 
    displays the progress of completed tasks.

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
            employee_name = user_info['name']
        else:
            print("Failed to retrieve employee details.")
            return
        
        # Calculate the number of completed tasks
        total_tasks = len(todos)
        completed_tasks = [task['title'] for task in todos if task['completed']]
        completed_count = len(completed_tasks)
        
        # Print the employee's task progress
        print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task}")
    else:
        print("Failed to retrieve TODO list.")

if __name__ == "__main__":
    """
    Main function to handle command-line argument and call the function 
    to get the employee TODO progress.
    """
    # Check if employee ID was passed as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command-line arguments
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for employee ID.")

