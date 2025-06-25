# To-Do-List-Application
# todo.py

from add_task import add_task
from remove_task import remove_task
from view_tasks import view_tasks

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
