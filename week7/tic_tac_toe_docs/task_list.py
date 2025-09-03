import sys

def add_task(tasks, task):
    """Add a task with its status set to False (incomplete)."""
    tasks.append((task, False))

def mark_task_completed(tasks, index):
    """Mark a task as completed by setting the status to True."""
    if 0 <= index < len(tasks):
        tasks[index] = (tasks[index][0], True)
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    """Delete a task from the list."""
    if 0 <= index < len(tasks):
        del tasks[index]
    else:
        print("Invalid task index.")

def list_tasks(tasks):
    """List all tasks with their completion status."""
    if not tasks:
        print("No tasks available.")
        return

    for i, (description, completed) in enumerate(tasks):
        print(f"{i + 1}. {'[X]' if completed else '[ ]'} {description}")

def sort_tasks(tasks):
    """Sort tasks alphabetically by description."""
    tasks.sort(key=lambda x: x[0])

def binary_search(tasks, target):
    """Perform a binary search for a task by description."""
    low, high = 0, len(tasks) - 1
    while low <= high:
        mid = (low + high) // 2
        if tasks[mid][0] == target:
            return mid
        elif tasks[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    tasks = []

    while True:
        print("\n1. Add Task")
        print("2. Mark Task Completed")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Sort Tasks")
        print("6. Search Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(tasks, task)
        elif choice == "2":
            try:
                index = int(input("Enter task index to mark as completed: ")) - 1
                mark_task_completed(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            try:
                index = int(input("Enter task index to delete: ")) - 1
                delete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            sort_tasks(tasks)
            print("Tasks sorted.")
        elif choice == "6":
            target = input("Enter task description to search: ")
            index = binary_search(tasks, target)
            if index != -1:
                print(f"Task '{target}' found at index {index + 1}.")
            else:
                print(f"Task '{target}' not found.")
        elif choice == "7":
            sys.exit("Exiting program.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
