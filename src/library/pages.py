from fastapi import APIRouter, Request, Depends, Form
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from starlette.templating import Jinja2Templates

from src.db.database import get_async_session
from src.library.models import Book, Author, Genre, Comment
from src.library.schemas import CreateComment

page_router = APIRouter(
    prefix='',
    tags=['library']
)

templates = Jinja2Templates(directory="src/templates")

@page_router.get("/")
async def main_page(
        request: Request,
        session: AsyncSession = Depends(get_async_session)
):
    query = await session.execute(select(Book).options(joinedload(Book.author), joinedload(Book.genre)).limit(4))
    book_list = query.scalars().all()
    return templates.TemplateResponse("main.html", {"request": request, "book_list": book_list})


@page_router.get('/newbook')
async def get_books(
        request: Request,
        session: AsyncSession = Depends(get_async_session)
):
    query = await session.execute(select(Book).options(joinedload(Book.author), joinedload(Book.genre)))
    book_list = query.scalars().all()
    return templates.TemplateResponse("newbook.html", {"request": request, "book_list": book_list})


@page_router.get('/popularbook')
async def get_pop_books(
        request: Request,
        session: AsyncSession = Depends(get_async_session)
):
    #session.query(Comment.course_id,func.count(Comment.course_id)).group_by(Comment.course_id).order_by(desc(func.count(Comment.course_id))).all()
    query = await session.execute(select(Book).options(joinedload(Book.author), joinedload(Book.genre)))
    pop_book_list = query.scalars().all()
    return templates.TemplateResponse("popular.html", {"request": request, "pop_book_list": pop_book_list})


@page_router.get('/book/{book_name}')
async def get_detail_book(
        book_name: str,
        request: Request,
        session: AsyncSession = Depends(get_async_session)
):
    query = await session.execute(select(Book).where(Book.name == book_name).options(joinedload(Book.author), joinedload(Book.comment), joinedload(Book.genre)))
    book = query.scalar()
    return templates.TemplateResponse("bookdetail.html", {"request": request, "book": book})


@page_router.post('/book/createcomment')
async def createcomment(
        request: Request,
        book_name: str,
        name: str = Form(),
        text: str = Form(),
        session: AsyncSession = Depends(get_async_session)
):
    comment = {
        'name': name,
        'text': text,
    }
    statement = insert(Comment).values(**comment)
    await session.execute(statement)
    await session.commit()
    return comment


@page_router.get('/authors')
async def get_authors(
        request: Request,
        session: AsyncSession = Depends(get_async_session)
):
    #session.query(Comment.course_id,func.count(Comment.course_id)).group_by(Comment.course_id).order_by(desc(func.count(Comment.course_id))).all()
    query = await session.execute(select(Author).order_by(Author.name))
    author_list = query.scalars().all()
    return templates.TemplateResponse("author.html", {"request": request, "author_list": author_list})


@page_router.get('/genres')
async def get_genres(
        request: Request,
        session: AsyncSession = Depends(get_async_session)
):
    query = await session.execute(select(Genre).order_by(Genre.name))
    genre_list = query.scalars().all()
    return templates.TemplateResponse("genre.html", {"request": request, "genre_list": genre_list})


@page_router.get("/about")
def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@page_router.get("/contact")
def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})