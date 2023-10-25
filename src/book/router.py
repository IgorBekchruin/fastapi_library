from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, insert, update, delete, func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from src.book.service import BookService

from src.db.database import get_async_session
from .models import Genre, Author, Comment, Book
from .schemas import *

router = APIRouter(
    prefix='/book',
    tags=['Book']
)


@router.get('/')
async def get_list_books() -> list[ViewBook]:
    return await BookService.find_all_objects()


@router.get('/{book_id}')
async def get_newlist_books(book_id: int) -> ViewBook:
    return await BookService.find_one_object_by_id(book_id)


@router.post('/add_book')
async def create_book(book: CreateBook):
    return await BookService.create_object(book)


@router.put('/{book_id}')
async def update_book(book_id: int, book: CreateBook):
    return await BookService.update_object(book_id, book)


@router.delete('/{book_id}')
async def delete_book(book_id: int):
    return await BookService.delete_object(book_id)