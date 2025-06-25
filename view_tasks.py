# view_tasks.py

from tasks import load_tasks

def view_tasks():
    tasks = load_tasks()
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
