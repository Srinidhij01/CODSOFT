def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

def add_task():
    task = input("Enter task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def remove_task():
    show_tasks()
    tasks = open("tasks.txt").readlines()
    try:
        num = int(input("Enter task number to remove: ")) - 1
        if 0 <= num < len(tasks):
            del tasks[num]
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
