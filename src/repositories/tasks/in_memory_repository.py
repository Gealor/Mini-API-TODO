from typing import Any
from typing import Dict
from typing import List

from core.database import Database
from core.database import db
from core.logger import log
from repositories.tasks.base_repository import BaseTaskRepository
from schemas.tasks import ListTaskReadSchema
from schemas.tasks import TaskCreateSchema
from schemas.tasks import TaskReadSchema


class TaskInMemoryRepository(BaseTaskRepository):
    def __init__(self, database: Database = db):
        self._database = database

    def get_all_tasks(self) -> ListTaskReadSchema:
        result = self._database.tasks
        log.info("Получено %d записей", len(result))

        return ListTaskReadSchema(
            tasks=[TaskReadSchema.model_validate(obj) for obj in result]
        )

    def get_task_by_id(self, task_id: int) -> TaskReadSchema | None:
        result = self._database.find_record_by_id(task_id)
        if result is None:
            return None

        return TaskReadSchema.model_validate(result)

    def create_task(self, task: TaskCreateSchema) -> TaskReadSchema:
        result = self._database.add_new_record(task.model_dump())
        return TaskReadSchema.model_validate(result)


