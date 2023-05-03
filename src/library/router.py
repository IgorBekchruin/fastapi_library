from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, insert, update, delete, func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.db.database import get_async_session
from .models import Genre, Author, Comment, Book
from .schemas import *

book_router = APIRouter(
    prefix='/library',
    tags=['library']
)


# CRUD and views for Genre model
@book_router.get('/genres')
async def get_list_genre(session: AsyncSession = Depends(get_async_session)):
    res = await session.execute(select(Genre).order_by(Genre.name))
    return res.scalars().all()


@book_router.post('/genres')
async def create_genre(
        genre: CreateGenre,
        session: AsyncSession = Depends(get_async_session)
):
    statement = insert(Genre).values(**genre.dict())
    await session.execute(statement)
    await session.commit()
    return {
        'status': '200',
        'genre': genre
    }


@book_router.put('/genres/{item_id}')
async def update_genre(
        item_id: int,
        genre: CreateGenre,
        session: AsyncSession = Depends(get_async_session)
):
    statement = update(Genre).where(Genre.id == item_id).values(**genre.dict())
    await session.execute(statement)
    await session.commit()
    return {
        'status': '200',
        'genre': genre
    }


@book_router.delete('/genres/{item_id}')
async def delete_genre(
        item_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await session.execute(delete(Genre).where(Genre.id == item_id))
    await session.commit()
    return {
        'status': '200',
        'water': f'genre {item_id} was deleted'
    }


# --------end views genres----------

# CRUD and views for Author model
@book_router.get('/author')
async def get_list_author(session: AsyncSession = Depends(get_async_session)):
    resault = await session.execute(select(Author).order_by(Author.name))
    return resault.scalars().all()


@book_router.post('/author')
async def create_author(
        author: CreateAuthor,
        session: AsyncSession = Depends(get_async_session)
):
    statement = insert(Author).values(**author.dict())
    await session.execute(statement)
    await session.commit()
    return {
        'status': '200',
        'genre': author
    }


@book_router.put('/author/{item_id}')
async def update_author(
        item_id: int,
        author: CreateAuthor,
        session: AsyncSession = Depends(get_async_session)
):
    statement = update(Author).where(Author.id == item_id).values(**author.dict())
    await session.execute(statement)
    await session.commit()
    return {
        'status': '200',
        'genre': author
    }


@book_router.delete('/author/{item_id}')
async def delete_author(
        item_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await session.execute(delete(Author).where(Author.id == item_id))
    await session.commit()
    return {
        'status': '200',
        'water': f'Author {item_id} was deleted'
    }


# ----------end views author-----------


# Views for comment
@book_router.get('/book/comments/{book_id}')
async def get_list_comments(
        book_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    resault = await session.execute(select(Comment).order_by(Comment.created_at.desc()))
    return resault.scalars().all()


@book_router.post('/book/comments')
async def create_comment(
        comment: CreateComment,
        session: AsyncSession = Depends(get_async_session)
):
    statement = insert(Comment).values(**comment.dict())
    await session.execute(statement)
    await session.commit()
    return {
        'status': '200',
        'genre': comment
    }


@book_router.delete('/book/comments/{item_id}')
async def delete_comment(
        item_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await session.execute(delete(Comment).where(Comment.id == item_id))
    await session.commit()
    return {
        'status': '200',
        'water': f'Comment {item_id} was deleted'
    }


# -----------end comment---------------

# ------Book views-----
@book_router.get('/book')
async def get_list_books(session: AsyncSession = Depends(get_async_session)):
    resault = await session.execute(select(Book).order_by(Book.name))
    return resault.scalars().all()


@book_router.get('/newbook')
async def get_newlist_books(session: AsyncSession = Depends(get_async_session)):
    resault = await session.execute(select(Book).order_by(Book.data.desc()))
    return resault.scalars().all()


@book_router.post('/book')
async def create_book(
        book: CreateBook,
        session: AsyncSession = Depends(get_async_session)
):
    statement = insert(Book).values(**book.dict())
    await session.execute(statement)
    await session.commit()
    return {
        'status': '200',
        'genre': book
    }


@book_router.put('/book/{item_id}')
async def update_book(
        item_id: int,
        book: CreateBook,
        session: AsyncSession = Depends(get_async_session)
):
    statement = update(Book).where(Book.id == item_id).values(**book.dict())
    await session.execute(statement)
    await session.commit()
    return {
        'status': '200',
        'genre': book
    }


@book_router.delete('/book/{item_id}')
async def delete_book(
        item_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await session.execute(delete(Book).where(Book.id == item_id))
    await session.commit()
    return {
        'status': '200',
        'water': f'Book {item_id} was deleted'
    }
# ----------
