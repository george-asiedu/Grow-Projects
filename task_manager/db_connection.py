from pymongo import MongoClient

client = MongoClient("mongodb+srv://task_manager:task_manager@grow-projects.hf7hilz.mongodb.net/")
db = client["task_manager"]
tasks_collection = db["tasks"]