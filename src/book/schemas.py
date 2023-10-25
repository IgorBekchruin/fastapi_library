import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class BaseBook(BaseModel):
    name: str
    data: datetime.datetime
    annotate: str

    model_config = ConfigDict(from_attributes=True)


class CreateBook(BaseBook):
    author_id: Optional[int] = None
    genre_id: Optional[int] = None


class ViewBook(CreateBook):
    id: int

