from sqlalchemy import func, select

from src.author.models import Author
from src.base_service.base_service import BaseService
from src.book.models import Book
from src.database import async_session


class AuthorService(BaseService):
    model = Author

    @classmethod
    async def find_all_objects_for_pages(cls):
        async with async_session() as session:
            query = (
                select(
                    cls.model.id,
                    cls.model.name,
                    func.count(Book.id).label("count_book"),
                )
                .select_from(cls.model)
                .join(Book, Book.author_id == cls.model.id)
                .group_by(cls.model.id)
                .order_by(cls.model.name)
            )
            res = await session.execute(query)
            return res.mappings().all()
