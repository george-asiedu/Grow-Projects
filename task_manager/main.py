from task_manager import tasks

def print_task_table(task_list):
    """Pretty print tasks in a table"""
    if not task_list:
        print("No tasks available.")
        return

    header = f"{'ID':<24} | Task"
    separator = "-" * 50
    rows = [f"{str(t['_id']):<24} | {t['task']}" for t in task_list]

    print("\n".join([header, separator] + rows))

def menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Get Task by ID")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter new task: ")
            print(tasks.add_task(task))

        elif choice == "2":
            task_list = tasks.get_all_tasks()
            print_task_table(task_list)

        elif choice == "3":
            task_id = input("Enter task ID: ")
            task = tasks.get_task_by_id(task_id)
            if task:
                print_task_table([task])
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = input("Enter task ID to update: ")
            new_task = input("Enter new task: ")
            print(tasks.update_task(task_id, new_task))

        elif choice == "5":
            task_id = input("Enter task ID to delete: ")
            print(tasks.delete_task(task_id))

        elif choice == "6":
            print("Exiting Task Manager...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()