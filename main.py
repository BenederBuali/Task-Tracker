import os
import json

class Task:
    def __init__(self, text, done=False):
        self.text = text
        self.done = done

tasks: Task = []

def _main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        match choice:
            case "1":
                add_task()
            case "2":
                view_task()
            case "3":
                mark_done()
            case "4":
                remove_task()
            case "5":
                break
            case _:
                print("Please choose a valid option")

def add_task():
    description = input("Task you want to add: ")

    task = Task(description, False)
    tasks.append(task)
    save_tasks()

def view_task():
    for index, task in enumerate(tasks, start=1):
        status = "x" if task.done else " "
        print(f"{index}. [{status}] {task.text}")

def mark_done():
    try:
        task_number = input("Task you want to set done: ")
        task_number = int(task_number)
        tasks[task_number - 1].done = True
    except (ValueError, IndexError):
        print("It has to be a number in the right reach")
    save_tasks()
    
def remove_task():
    try:
        task_number = input("Which Task do you want to delete: ")
        task_number = int(task_number)
        tasks.pop(task_number-1)
    except (ValueError, IndexError):
        print("It has to be a number in the right reach")
    save_tasks()

def show_menu():
    print("1. Add Task\n" \
    "2. View Task\n" \
    "3. Mark task as done\n" \
    "4. Remove Task\n" \
    "5. Exit")

def save_tasks():
    os.makedirs("todo-list/data", exist_ok=True)
    data = [{"text": t.text, "done": t.done} for t in tasks]
    with open("todo-list/data/tasks.json", "w") as f:
        json.dump(data, f)

def load_tasks():
    global tasks
    try:
        with open("todo-list/data/tasks.json", "r") as f:
            data = json.load(f)
        tasks = [Task(item["text"], item["done"]) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

load_tasks()
_main()