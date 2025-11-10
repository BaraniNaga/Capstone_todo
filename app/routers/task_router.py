from fastapi import APIRouter, HTTPException
from app.schemas.task_schema import Task, TaskCreate, TaskUpdate
from app.crud.task_crud import (
    create_task,
    list_tasks,
    get_task,
    update_task,
    delete_task
)


router = APIRouter()

@router.post("/", response_model=Task, status_code=201)
def create(payload: TaskCreate):
    return create_task(payload)


@router.get("/", response_model=list[Task])
def get_all():
    return list_tasks()


@router.get("/{task_id}", response_model=Task)
def get_one(task_id: int):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=Task)
def update(task_id: int, payload: TaskUpdate):
    task = update_task(task_id, payload)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}", status_code=204)
def delete(task_id: int):
    result = delete_task(task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
