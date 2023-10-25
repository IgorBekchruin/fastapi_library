from src.base_service.base_service import BaseService
from src.book.models import Genre


class GenreService(BaseService):
    model = Genre