# Importing required modules
import json
import os
from tabulate import tabulate  # Install using `pip install tabulate`

# A dictionary to store student details
students = {}

# Define the file path
file_path = r"D:\PythonProject\python program\students.json"

# Function to add a new student
def add_student(student_id, name, age, major):
    """Adds a new student to the system."""
    try:
        if student_id in students:
            raise ValueError("Student ID already exists.")
        students[student_id] = {
            "name": name,
            "age": age,
            "major": major
        }
        print(f"Student {name} added successfully!")
    except ValueError as ve:
        print(f"Error: {ve}")

# Function to retrieve student details by ID
def get_student(student_id):
    """Retrieves the details of a student by their ID."""
    try:
        if student_id not in students:
            raise KeyError("Student ID not found.")
        return students[student_id]
    except KeyError as ke:
        print(f"Error: {ke}")
        return None

# Function to delete a student
def delete_student(student_id):
    """Deletes a student from the system."""
    try:
        if student_id not in students:
            raise KeyError("Student ID not found.")
        del students[student_id]
        print(f"Student {student_id} deleted successfully!")
    except KeyError as ke:
        print(f"Error: {ke}")

# Function to save student details to a file
def save_to_file():
    """Saves student details to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(students, file)
        print(f"Data saved to {file_path}.")
    except IOError as io:
        print(f"Error saving to file: {io}")

# Function to load student details from a file
def load_from_file():
    """Loads student details from a JSON file."""
    try:
        global students
        if not os.path.exists(file_path):
            raise FileNotFoundError("The specified file does not exist.")
        with open(file_path, 'r') as file:
            students = json.load(file)
        print(f"Data loaded from {file_path}.")
    except FileNotFoundError as fnf:
        print(f"Error: {fnf}")
    except json.JSONDecodeError:
        print(f"Error: File {file_path} is not in valid JSON format.")

# Function to view all students in a table format
def view_all_students():
    """Displays all student details in a tabular format."""
    if not students:
        print("No student records available.")
    else:
        # Convert student data into a list of lists for tabulate
        table_data = [[student_id, details["name"], details["age"], details["major"]]
                      for student_id, details in students.items()]
        headers = ["Student ID", "Name", "Age", "Major"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
