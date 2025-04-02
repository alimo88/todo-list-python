def show_menu():
    print("\n📋 TO-DO LIST MENU")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")


def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\n📝 Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No task file found. Starting fresh!")

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:  # 'a' means append
        file.write(task + "\n")
    print("✅ Task added.")

def remove_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to remove: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"❌ Removed: {removed.strip()}")
        else:
            print("⚠️ Invalid number. Try again.")
    except ValueError:
        print("⚠️ Please enter a number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("👋 Goodbye! See you later.")
        break
    else:
        print("⚠️ Invalid choice. Please enter 1, 2, 3 or 4.")
