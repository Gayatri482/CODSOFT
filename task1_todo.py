
# Task 1: To-Do List App (Simple, Unique Version)
import datetime

todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task['task']} (Added: {task['time']})")

def add_task():
    task = input("Enter task: ")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    todo_list.append({"task": task, "time": time})
    print("Task added.")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(todo_list):
        removed = todo_list.pop(num - 1)
        print(f"Removed: {removed['task']}")

def menu():
    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

menu()
