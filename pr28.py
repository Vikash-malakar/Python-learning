from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI(
    title="Task Management API",
    description="Simple REST API built with Python and FastAPI",
    version="1.0.0"
)

FILE_NAME = "tasks.json"


class Task(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


# Home
@app.get("/")
def home():
    return {
        "message": "Task Management API is running!",
        "docs": "/docs"
    }


# Get all tasks
@app.get("/tasks")
def get_tasks():
    return load_tasks()


# Get single task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# Create task
@app.post("/tasks")
def create_task(task: Task):
    tasks = load_tasks()

    new_id = 1

    if tasks:
        new_id = max(item["id"] for item in tasks) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks.append(new_task)

    save_tasks(tasks)

    return {
        "message": "Task created successfully",
        "task": new_task
    }


# Update task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:

            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed

            save_tasks(tasks)

            return {
                "message": "Task updated successfully",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:

            tasks.remove(task)

            save_tasks(tasks)

            return {
                "message": "Task deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )