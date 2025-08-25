def update_task(task_list, old_task, new_task):
    if old_task in task_list:
        index = task_list.index(old_task)
        task_list[index] = new_task
        return f"Task '{old_task}' updated to '{new_task}'. Current tasks: {task_list}"
    else:
        return f"Task '{old_task}' not found in the list."