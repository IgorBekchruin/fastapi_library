from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, insert, update, delete, func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.author.service import AuthorService

from src.db.database import get_async_session
from .models import Genre, Author, Comment, Book
from .schemas import *

router = APIRouter(
    prefix='/author',
    tags=['Author']
)


# CRUD and views for Author model
@router.get('/')
async def get_list_author() -> list[ViewAuthor]:
    return await AuthorService.find_all_objects()


@router.get('/{author_id}')
async def get_one_author(author_id: int) -> ViewAuthor:
    return AuthorService.find_one_object_by_id(author_id)


@router.post('/add_author')
async def create_author(author: CreateAuthor):
    return await AuthorService.create_object(author)


@router.put('/{author_id}')
async def update_author(
        author_id: int,
        author: CreateAuthor
):
    return await AuthorService.update_object(author_id, author)


@router.delete('/{author_id}')
async def delete_author(author_id: int):
    return await AuthorService.delete_object(author_id)