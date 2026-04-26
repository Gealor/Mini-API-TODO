
from repositories.tasks.base_repository import BaseTaskRepository
from schemas.exceptions import TaskNotFoundException
from schemas.tasks import ListTaskReadSchema
from schemas.tasks import TaskCreateSchema
from schemas.tasks import TaskReadSchema


class TaskService:
    def __init__(self, repository: BaseTaskRepository):
        self.repo = repository

    def get_all_tasks(self) -> ListTaskReadSchema:
        result = self.repo.get_all_tasks()

        return result

    def get_task_by_id(self, task_id: int) -> TaskReadSchema:
        result = self.repo.get_task_by_id(task_id)

        if result is None:
            raise TaskNotFoundException

        return result

    def create_task(self, data: TaskCreateSchema) -> TaskReadSchema:
        result = self.repo.create_task(task=data)

        return result
