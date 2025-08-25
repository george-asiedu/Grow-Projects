def show_tasks(task_list):
    if not task_list:
        return "No tasks available."
    return "Current tasks:\n" + "\n".join(f"- {task}" for task in task_list)