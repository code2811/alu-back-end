#!/usr/bin/python3
"""
Script to export all employee task data to JSON format
"""
import json
import requests
import sys

def get_all_employee_tasks():
    """
    Fetches and formats all employee tasks from the API
    Returns: Dictionary with employee IDs as keys and lists of task dictionaries as values
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get all users first
    users_response = requests.get(f"{base_url}/users")
    users = users_response.json()
    
    # Initialize the result dictionary
    all_tasks = {}
    
    # For each user, get their tasks and format them
    for user in users:
        user_id = str(user['id'])  # Convert ID to string to match example format
        username = user['username']
        
        # Get tasks for this user
        tasks_response = requests.get(f"{base_url}/users/{user_id}/todos")
        tasks = tasks_response.json()
        
        # Format tasks according to requirements
        formatted_tasks = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in tasks
        ]
        
        # Add to main dictionary
        all_tasks[user_id] = formatted_tasks
    
    return all_tasks

def export_to_json():
    """
    Main function to export all tasks to JSON file
    """
    try:
        # Get all tasks
        all_tasks = get_all_employee_tasks()
        
        # Write to JSON file
        with open('todo_all_employees.json', 'w') as jsonfile:
            json.dump(all_tasks, jsonfile)
            
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    export_to_json()
