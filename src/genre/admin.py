from sqladmin import ModelView

from src.book.models import Genre


class GenreAdmin(ModelView, model=Genre):
    column_list = [Genre.id, Genre.name]
