

tasks = []
next_task_id = 1


def add_task():
   
    global next_task_id

    description = input("Enter task description: ").strip()

    if not description:
        print("Error: Task description cannot be empty.")
        return

    task = {
        "id": next_task_id,
        "description": description,
        "status": "Pending"
    }

    tasks.append(task)

    print("\nTask added successfully!")
    print("ID:", task["id"])
    print("Task:", task["description"])
    print("Status:", task["status"])

    next_task_id += 1


def view_tasks():
   
    if not tasks:
        print("\nNo tasks found. Please add a task first.")
        return

    print("\n========== ALL TASKS ==========")

    for task in tasks:
        print("-" * 30)
        print("ID:", task["id"])
        print("Task:", task["description"])
        print("Status:", task["status"])

    print("-" * 30)


def find_task(task_id):
  
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def update_task():
   
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Error: Please enter a valid numeric ID.")
        return

    task = find_task(task_id)

    if task is None:
        print("Error: Task ID not found.")
        return

    new_description = input("Enter new task description: ").strip()

    if not new_description:
        print("Error: Task description cannot be empty.")
        return

    task["description"] = new_description

    print("Task updated successfully!")


def complete_task():
   
    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Error: Please enter a valid numeric ID.")
        return

    task = find_task(task_id)

    if task is None:
        print("Error: Task ID not found.")
        return

    if task["status"] == "Completed":
        print("This task is already completed.")
        return

    task["status"] = "Completed"

    print("Task marked as completed successfully!")


def delete_task():
   
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Error: Please enter a valid numeric ID.")
        return

    task = find_task(task_id)

    if task is None:
        print("Error: Task ID not found.")
        return

    tasks.remove(task)

    print("Task deleted successfully!")


def display_menu():
  
    print("\n====== TODO APPLICATION ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")


def main():
   
    print("Welcome to the TODO Application!")

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            complete_task()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            print("Thank you for using the TODO Application!")
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 6.")


# Start the application
if __name__ == "__main__":
    main()
