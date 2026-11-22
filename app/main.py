
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="DevOps Task Manager")

# Temporary task storage
tasks = []

# Define task structure
class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to DevOps Task Manager!",
        "status": "Application is running"
    }


# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Create a task
@app.post("/tasks")
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        **task.model_dump()
    }

    tasks.append(new_task)
    return new_task


# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# Get task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")
