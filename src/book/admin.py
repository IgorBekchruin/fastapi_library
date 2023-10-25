from sqladmin import ModelView

from src.book.models import Book



class BookAdmin(ModelView, model=Book):
    column_list = [Book.id, Book.name, Book.author_id, Book.genre_id]