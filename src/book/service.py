import os

from sqlalchemy import select

from src.base_service.base_service import BaseService
from src.book.models import Book
from src.database import async_session
from src.utils.save_image import image_add_origin
from src.utils.translate import translate_name


class BookService(BaseService):
    model = Book

    @classmethod
    async def add_new_book(cls, book_data):
        translit_book_name = translate_name(book_data.name)
        path_folder = f"src/static/images/books/{translit_book_name}"
        if not os.path.exists(path_folder):
            os.mkdir(path_folder)

        path_image = image_add_origin(book_data.image, path_folder, translit_book_name)

        async with async_session() as session:
            new_book = cls.model(
                name=book_data.name,
                data=book_data.data,
                annotate=book_data.annotate,
                image=path_image[11:],
                pages=book_data.pages,
                rating=book_data.rating,
                author_id=book_data.author_id,
                genre_id=book_data.genre_id,
            )
            session.add(new_book)
            await session.commit()

        return new_book

    @classmethod
    async def find_detail_book(cls, book_name: str):
        async with async_session() as session:
            query = select(cls.model).filter_by(name=book_name)
            res = await session.execute(query)
            return res.scalars().unique().one_or_none()

    @classmethod
    async def find_books_by_filter(cls, param_dict):
        async with async_session() as session:
            query = select(cls.model).filter_by(**param_dict)
            res = await session.execute(query)
            return res.scalars().all()
