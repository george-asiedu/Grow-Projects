from db_connection import tasks_collection
from bson.objectid import ObjectId

def add_task(task: str):
    """Add a new task to MongoDB"""
    result = tasks_collection.insert_one({"task": task})
    return f"Task added with id: {result.inserted_id}"

def get_all_tasks():
    """Retrieve all tasks as a list of dicts"""
    return list(tasks_collection.find({}, {"_id": 1, "task": 1}))

def get_task_by_id(task_id: str):
    """Retrieve a single task by its MongoDB _id"""
    try:
        task = tasks_collection.find_one({"_id": ObjectId(task_id)}, {"_id": 1, "task": 1})
        if task:
            return task
        else:
            return None
    except Exception:
        return None

def update_task(task_id: str, new_task: str):
    """Update a task by its MongoDB _id"""
    try:
        result = tasks_collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"task": new_task}}
        )
        if result.modified_count > 0:
            return f"Task with id {task_id} updated to '{new_task}'."
        else:
            return "Task not found or no changes made."
    except Exception:
        return "Invalid task ID format."

def delete_task(task_id: str):
    """Delete a task by its MongoDB _id"""
    try:
        result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
        if result.deleted_count > 0:
            return f"Task with id {task_id} deleted."
        else:
            return "Task not found."
    except Exception:
        return "Invalid task ID format."