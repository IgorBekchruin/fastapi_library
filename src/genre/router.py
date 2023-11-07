from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.genre.service import GenreService

from .schemas import *

router = APIRouter(prefix="/genre", tags=["Genre"])


@router.get("/")
@cache(expire=60 * 3)
async def get_list_genre() -> list[ViewGenre]:
    return await GenreService.find_all_objects(30)


@router.post("/add_genre")
async def create_genre(genre: CreateGenre):
    return await GenreService.create_object(genre)


@router.put("/{genre_id}")
async def update_genre(genre_id: int, genre: CreateGenre):
    return await GenreService.update_object(genre_id, genre)


@router.delete("/{genre_id}")
async def delete_genre(genre_id: int):
    return await GenreService.delete_object(genre_id)
