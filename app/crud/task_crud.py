from datetime import datetime
from app.db.memory_db import tasks, next_id
from app.models.task import TaskModel
from app.schemas.task_schema import TaskCreate, TaskUpdate


def create_task(payload: TaskCreate) -> TaskModel:
    global next_id
    now = datetime.utcnow()

    task = TaskModel(
        id=next_id,
        title=payload.title,
        description=payload.description,
        completed=payload.completed,
        created_at=now,
        updated_at=now
    )

    tasks.append(task)
    next_id += 1
    return task


def list_tasks():
    return tasks


def get_task(task_id: int):
    return next((t for t in tasks if t.id == task_id), None)


def update_task(task_id: int, payload: TaskUpdate):
    task = get_task(task_id)
    if not task:
        return None

    if payload.title is not None:
        task.title = payload.title

    if payload.description is not None:
        task.description = payload.description

    if payload.completed is not None:
        task.completed = payload.completed

    task.updated_at = datetime.utcnow()
    return task


def delete_task(task_id: int):
    global tasks
    task = get_task(task_id)
    if not task:
        return False
    tasks = [t for t in tasks if t.id != task_id]
    return True
