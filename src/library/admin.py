from sqladmin import ModelView

from src.library.models import Genre, Author, Comment, Book


class GenreAdmin(ModelView, model=Genre):
    column_list = [Genre.id, Genre.name]


class AuthorAdmin(ModelView, model=Author):
    column_list = [Author.id, Author.name]


class CommentAdmin(ModelView, model=Comment):
    column_list = [Comment.id, Comment.name, Comment.created_at]


class BookAdmin(ModelView, model=Book):
    column_list = [Book.id, Book.name, Book.author_id.name]