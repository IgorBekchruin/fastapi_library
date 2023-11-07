from sqladmin import ModelView

from src.author.models import Author


class AuthorAdmin(ModelView, model=Author):
    column_list = [Author.id, Author.name]
