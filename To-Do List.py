# Simple To-Do List 

# We will use a list to store tasks
todo_list = []

# Function to display all tasks
def show_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Function to add a task
def add_task():
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print(f'"{task}" has been added to your list.')

# Function to remove a task
def remove_task():
    show_tasks()
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed = todo_list.pop(task_number - 1)
            print(f'"{removed}" has been removed from your list.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as done (just for fun, shows ✔️)
def mark_done():
    show_tasks()
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1] += " ✔️"
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Show all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Mark a task as done")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_done()
    elif choice == '5':
        print("Goodbye! Have a productive day! 💪")
        break
    else:
        print("Please enter a valid choice (1 to 5).")
