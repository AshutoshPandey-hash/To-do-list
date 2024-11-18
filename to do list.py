tasks = []

def show_menu():
    print("\n--- To-Do-List Menu ---")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Remove task")
    print("4. Save tasks to file")
    print("5. Exit")

def view_tasks():
    if tasks:
        print("\n Your Tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\n your task list is empty!")

def add_tasks():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Task list cannot be empty")

def remove_tasks():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
             removed_task = tasks.pop(task_num-1)
             print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid input")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks():
    with open("tasks.txt", 'w') as f:
        for task in tasks:
            f.write(task + "\n")
    print("Tasks saved to 'tasks.txt'.")

while(True):
    show_menu()
    choice = input("choose an option: ").strip()
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_tasks()
    elif choice == "3":
        remove_tasks()
    elif choice == "4":
        save_tasks()
    elif choice == "5":
        print("Exiting to do list. Good-bye!")
        break
    else:
        print("Inavlid choice. Please select a valid option.")