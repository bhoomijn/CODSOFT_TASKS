
import json
from pathlib import Path

# File used to store tasks permanently
DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load saved tasks. Return an empty list if no saved file exists."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list) and all(isinstance(task, str) for task in data):
            return data

        print("Warning: Saved task data is invalid. Starting with an empty list.")
        return []

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved tasks. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True
    except OSError:
        print("Error: Tasks could not be saved.")
        return False


def show_tasks(tasks):
    """Display all tasks with numbering."""
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n========== YOUR TASKS ==========")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def add_task(tasks):
    task = input("Enter your new task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)
    if save_tasks(tasks):
        print("Task added successfully!")


def update_task(tasks):
    if not tasks:
        print("\nThere are no tasks to update.")
        return

    show_tasks(tasks)

    try:
        number = int(input("Enter the task number to update: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if not 1 <= number <= len(tasks):
        print("Invalid task number.")
        return

    new_task = input("Enter the updated task: ").strip()
    if not new_task:
        print("Task cannot be empty.")
        return

    tasks[number - 1] = new_task
    if save_tasks(tasks):
        print("Task updated successfully!")


def delete_task(tasks):
    if not tasks:
        print("\nThere are no tasks to delete.")
        return

    show_tasks(tasks)

    try:
        number = int(input("Enter the task number to delete: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if not 1 <= number <= len(tasks):
        print("Invalid task number.")
        return

    deleted_task = tasks.pop(number - 1)
    if save_tasks(tasks):
        print(f"Deleted task: {deleted_task}")


def main():
    tasks = load_tasks()
    print("Welcome to the To-Do List Application!")

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Your tasks are saved. Thank you for using the application!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
