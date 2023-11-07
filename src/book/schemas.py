import datetime
from dataclasses import dataclass
from typing import Optional

from fastapi import File, Form, UploadFile
from pydantic import BaseModel, ConfigDict

from src.author.schemas import BaseAuthor
from src.genre.schemas import BaseGenre


class BaseBook(BaseModel):
    name: str
    data: datetime.date
    annotate: str
    image: str
    pages: int
    rating: float
    author: BaseAuthor
    genre: BaseGenre

    model_config = ConfigDict(from_attributes=True)


@dataclass
class CreateBook:
    name: str = Form(...)
    data: datetime.date = Form(...)
    annotate: str = Form(...)
    image: UploadFile = File(...)
    pages: int = Form(...)
    rating: Optional[float] = Form()
    author_id: Optional[int] = Form()
    genre_id: Optional[int] = Form()


class ViewBook(BaseBook):
    id: int
