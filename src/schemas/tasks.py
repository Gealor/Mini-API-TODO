from enum import Enum

from pydantic import BaseModel
from pydantic import Field

from core.database import db
from schemas.base import BaseAppSchema


class TaskStatusEnum(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"


class BaseTaskSchema(BaseAppSchema):
    title: str = Field(examples=["Купить молоко", "Побриться", "Сдать лабораторную работу"])
    description: str | None = Field(default=None, examples=["2 литра", "Тестирование новой бритвы"])
    status: TaskStatusEnum = Field(examples=[TaskStatusEnum.done, TaskStatusEnum.in_progress, TaskStatusEnum.new])

    class Config:
        from_attributes = True

class TaskCreateSchema(BaseTaskSchema):
    pass

class TaskReadSchema(BaseTaskSchema):
    id: int

class ListTaskReadSchema(BaseAppSchema):
    tasks: list[TaskReadSchema]
