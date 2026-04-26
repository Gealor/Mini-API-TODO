from fastapi import Depends

from core.database import db
from repositories.tasks.base_repository import BaseTaskRepository
from repositories.tasks.in_memory_repository import TaskInMemoryRepository
from services.tasks_service import TaskService


def get_db():
    return db

def get_task_repository() -> BaseTaskRepository:
    return TaskInMemoryRepository(database = get_db())

def get_task_service() -> TaskService:
    return TaskService(repository=get_task_repository())
