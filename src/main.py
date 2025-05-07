import argparse
import json
from pathlib import Path
from datetime import datetime

# Define the file path where tasks will be stored
TASKS_FILE = Path("tasks.json")

def init_tasks_file():
    """Create an empty tasks file if it doesn't exist."""
    TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not TASKS_FILE.exists():
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)

def get_tasks():
    """Load tasks from the tasks.json file."""
    if not TASKS_FILE.exists():
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks to the tasks.json file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def generate_id():
    """Generate a unique ID for a new task."""
    if not get_tasks():
        return 1
    return max(task["id"] for task in get_tasks()) + 1

def add_task(description, status="in progress"):
    """Add a new task to the list."""
    tasks = get_tasks()
    task_id = generate_id()
    task = {
        "id": task_id,
        "description": description,
        "status": status,
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task_id} - {description}")

def update_task(index, description=None, status=None):
    """Update an existing task."""
    tasks = get_tasks()
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    task = tasks[index]
    if description:
        task["description"] = description
    if status:
        task["status"] = status
    task["updatedAt"] = datetime.now().isoformat()

    save_tasks(tasks)
    print(f"Task {index + 1} updated.")

def delete_task(index):
    """Delete a task."""
    tasks = get_tasks()
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    del tasks[index]
    save_tasks(tasks)
    print(f"Task {index + 1} deleted.")

def list_tasks(status=None):
    """List all tasks, optionally filtered by status."""
    tasks = get_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks):
        marker = "[X]" if task["status"] == "done" else "[ ]"
        if status is None or task["status"] == status:
            created_at = datetime.fromisoformat(task["createdAt"]).strftime("%Y-%m-%d %H:%M:%S")
            updated_at = datetime.fromisoformat(task["updatedAt"]).strftime("%Y-%m-%d %H:%M:%S")
            print(f"{index + 1}. {marker} {task['id']} - {task['description']} ({task['status']}) [Created: {created_at}, Updated: {updated_at}]")

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")
    add_parser.add_argument("--status", choices=["in progress", "done"], default="in progress", help="Task status")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("index", type=int, help="Task index")
    update_parser.add_argument("--description", type=str, nargs="?", help="New task description")
    update_parser.add_argument("--status", choices=["in progress", "done"], nargs="?", help="New task status")

    # Delete command
    subparsers.add_parser("delete", help="Delete a task").add_argument("index", type=int, help="Task index")

    # List all tasks
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--status", choices=["in progress", "done"], nargs="?", default=None, help="Filter by status")

    args = parser.parse_args()

    init_tasks_file()

    if args.command == "add":
        add_task(args.description, args.status)
    elif args.command == "update":
        update_task(args.index - 1, args.description, args.status)  # Convert to zero-based index
    elif args.command == "delete":
        delete_task(args.index - 1)  # Convert to zero-based index
    elif args.command == "list":
        list_tasks(args.status)

if __name__ == "__main__":
    main()