import os

# File to store tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file into a list."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks list to file."""
    with open(TASK_FILE, "w") as f:
        for t in tasks:
            f.write(t + "\n")

def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task."""
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added!")

def mark_done(tasks):
    """Mark a task as done."""
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1] = tasks[num-1] + " ✅"
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            save_tasks(tasks)
            print("Task deleted!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            tasks = load_tasks()  # reload updated file
        elif choice == "3":
            mark_done(tasks)
            tasks = load_tasks()
        elif choice == "4":
            delete_task(tasks)
            tasks = load_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
