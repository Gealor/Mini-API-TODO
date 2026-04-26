from abc import ABC
from abc import abstractmethod

from schemas.tasks import ListTaskReadSchema
from schemas.tasks import TaskCreateSchema
from schemas.tasks import TaskReadSchema


class BaseTaskRepository(ABC):
    @abstractmethod
    def get_all_tasks(self) -> ListTaskReadSchema:
        pass

    @abstractmethod
    def get_task_by_id(self, task_id: int) -> TaskReadSchema | None:
        pass

    @abstractmethod
    def create_task(self, task: TaskCreateSchema) -> TaskReadSchema:
        pass
