from src.base_service.base_service import BaseService
from src.book.models import Book


class BookService(BaseService):
    model = Book