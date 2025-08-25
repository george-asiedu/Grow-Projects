import add
import show
import update
import delete

add_new_task = input("Would you like to add a new task? (yes/no): ").strip().lower()
if add_new_task == 'yes':
    task_list = []
    task = input("Enter the task you want to add: ").strip()
    print(add.add_task(task_list, task))
else:
    print("No task added.")
    task_list = []

show_tasks = input("Would you like to see the current tasks? (yes/no): ").strip().lower()
if show_tasks == 'yes':
    print(show.show_tasks(task_list))
else:
    print("No tasks to show.")

update_task = input("Would you like to update a task? (yes/no): ").strip().lower()
if update_task == 'yes':
    old_task = input("Enter the task you want to update: ").strip()
    new_task = input("Enter the new task: ").strip()
    print(update.update_task(task_list, old_task, new_task))
else:
    print("No task updated.")

delete_task = input("Would you like to delete a task? (yes/no): ").strip().lower()
if delete_task == 'yes':
    print(delete.delete_tasks(task_list))
else:
    print("No task deleted.")