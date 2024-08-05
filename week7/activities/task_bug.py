'''A buggy Task Manager that provides an opportunity to debug code by both reasoning about it and stepping through using pdb.
The program has a number of bugs that are introduced one at a time. The goal is to find and fix the bugs.
Ensure you step through this program in pdb only to understand how the program works and to find the bugs.'''

import sys

def add_task(task):
    task.append((task, False)) 

def mark_task_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index] = True 
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.remove(tasks[index]) 
    else:
        print("Invalid task index.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        print(f"{i}. {'[X]' if task else '[ ]'} {task[0]}") 

def sort_tasks(tasks):
    tasks.sort(key=lambda x: x[0])

def binary_search(tasks, target):
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
            index = int(input("Enter task index to mark as completed: ")) - 1
            mark_task_completed(tasks, index)
        elif choice == "3":
            index = int(input("Enter task index to delete: ")) - 1
            delete_task(tasks, index)
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
