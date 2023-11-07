from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin
from starlette.staticfiles import StaticFiles

from src.author.admin import AuthorAdmin
from src.author.router import router as author_router
from src.book.admin import BookAdmin
from src.book.router import router as book_router
from src.config import settings
from src.database import engine
from src.genre.admin import GenreAdmin
from src.genre.router import router as genre_router
from src.pages.pages import page_router

app = FastAPI()

app.include_router(author_router)
app.include_router(genre_router)
app.include_router(book_router)
app.include_router(page_router)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

admin = Admin(app, engine)
admin.add_view(GenreAdmin)
admin.add_view(AuthorAdmin)
admin.add_view(BookAdmin)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
