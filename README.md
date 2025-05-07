# CLI Task Manager

A simple Command Line Interface (CLI) task manager written in Python.

## Project Structure

The project consists of three files:
- src/main.py: The main script for running the task manager.
- tasks.json: A JSON file to store tasks.
- src/example.py: An example Python file with a function to extract text between markers.

### Directory Layout
- src/example.py: An example Python file with a function to extract text between markers.

### Directory Layout
## Usage

### Installing Dependencies

No external dependencies are required. Ensure you have Python installed on your system.

### Running the Task Manager

To run the task manager, execute the following command in your terminal:

```sh
python src/main.py

## The CLI will provide options to add, update, delete, and list tasks.

## Example Commands
## Adding a Task:
python src/main.py add "Complete the project" --status done
## Updating a Task:
python src/main.py update 1 --description "Update project description"
## Deleting a Task:
python src/main.py delete 1
## Listing Tasks:
python src/main.py list --status done

## Example Function
## The src/example.py file contains an example function to extract text between markers:
def between_markers(text: str, start: str, end: str) -> str:
    return text[text.find(start) + len(start):text.find(end)


https://roadmap.sh/projects/task-tracker
