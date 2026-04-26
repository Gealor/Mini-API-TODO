from typing import Annotated, Any

from fastapi import APIRouter, Depends
from fastapi import HTTPException
from fastapi import status

from dependencies import get_task_service
from schemas.exceptions import TaskNotFoundException
from schemas.tasks import ListTaskReadSchema, TaskCreateSchema
from schemas.tasks import TaskReadSchema
from services.tasks_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"], dependencies=[Depends(get_task_service)])
type task_service_depends = Annotated[TaskService, Depends(get_task_service)]

@router.get("/")
def get_list_tasks(service: task_service_depends) -> ListTaskReadSchema:
    return service.get_all_tasks()

@router.get("/{id}")
def get_task_by_id(id: int, service: task_service_depends) -> TaskReadSchema:
    try:
        result = service.get_task_by_id(task_id=id)
    except TaskNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task by this ID not found"
        ) from e

    return result

@router.post("/")
def create_task(data: TaskCreateSchema, service: task_service_depends) -> TaskReadSchema:
    return service.create_task(data)



