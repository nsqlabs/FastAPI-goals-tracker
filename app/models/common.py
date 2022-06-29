from datetime import datetime as DateTime
from enum import Enum
from lib2to3.pytree import Base
from typing import Optional

from pydantic import BaseModel, Field, validator


class DateTimeModelMixin(BaseModel):
    created_at: DateTime = None  # type: ignore
    updated_at: DateTime = None  # type: ignore

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(
        cls,  # noqa: N805
        value: DateTime,  # noqa: WPS110
    ) -> DateTime:
        return value or DateTime.now()


class IDModelMixin(BaseModel):
    id_: int = Field(..., alias="id")


class TimeTrackedModelMixin(BaseModel):
    spent_time_in_hours: int = Field(0, alias="spent_time_in_hours")
    
class Status(Enum):
    BACKLOG = 0
    NEXT = 1
    IN_PROGRESS = 2
    REVIEW = 3
    DONE = 4
    ARCHIVED = 5


class CommonOrganizationInfoModelMixin(TimeTrackedModelMixin, IDModelMixin, DateTimeModelMixin, BaseModel):
    archived: bool = False
    completion_date: Optional[DateTime]
    description: Optional[str] = ''
    due_date: Optional[DateTime]
    favorite: bool = False
    name: str
    status: Status
    user_id: str
