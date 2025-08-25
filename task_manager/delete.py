def delete_tasks(task_list):
    if not task_list:
        return "No tasks available to delete."

    print("Current tasks:")
    for i, task in enumerate(task_list, start=1):
        print(f"{i}. {task}")

    try:
        task_number = int(input("Enter the number of the task you want to delete: "))
        if 1 <= task_number <= len(task_list):
            deleted_task = task_list.pop(task_number - 1)
            return f"Task '{deleted_task}' deleted. Remaining tasks: {task_list}"
        else:
            return "Invalid task number."
    except ValueError:
        return "Please enter a valid number."