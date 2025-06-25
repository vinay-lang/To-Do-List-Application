# add_task.py

from tasks import load_tasks, save_tasks

def add_task():
    tasks = load_tasks()
    new_task = input("Enter the task to add: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{new_task}' added.")
