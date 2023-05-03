from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel
from datetime import date

class BaseGenre(BaseModel):
    name: str


class CreateGenre(BaseGenre):
    pass

    class Config:
        orm_mode = True


class ViewGenre(BaseGenre):
    id: int


class BaseAuthor(BaseModel):
    name: str
    birthday: date
    description: str


class CreateAuthor(BaseAuthor):
    pass

    class Config:
        orm_mode = True


class ViewAuthor(BaseAuthor):
    id: int


class BaseComment(BaseModel):
    name: str
    text: str

@dataclass
class CreateComment(BaseComment):
    created_at: date

    class Config:
        orm_mode = True


class ViewComment(BaseComment):
    id: int
    created_at: date


class BaseBook(BaseModel):
    name: str
    annotate: str


class CreateBook(BaseBook):
    author_id: Optional[int] = None
    genre_id: Optional[int] = None

    class Config:
        orm_mode = True

class ViewBook(BaseBook):
    id: int
    author_id: int
