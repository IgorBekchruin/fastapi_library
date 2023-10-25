from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from starlette.staticfiles import StaticFiles

from .database import engine
from src.library.admin import GenreAdmin, AuthorAdmin, CommentAdmin, BookAdmin
from src.library.pages import page_router
from src.library.router import book_router

app = FastAPI(
    title='MyLib'
)

app.include_router(book_router)
app.include_router(page_router)

app.mount("/static", StaticFiles(directory='static'), name="static")

admin = Admin(app, engine)
admin.add_view(GenreAdmin)
admin.add_view(AuthorAdmin)
admin.add_view(CommentAdmin)
admin.add_view(BookAdmin)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


