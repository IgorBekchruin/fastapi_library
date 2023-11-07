from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.author.schemas import CreateAuthor, ViewAuthor
from src.author.service import AuthorService

router = APIRouter(prefix="/author", tags=["Author"])


# CRUD and views for Author model
@router.get("/")
@cache(expire=60 * 3)
async def get_list_author() -> list[ViewAuthor]:
    return await AuthorService.find_all_objects(30)


@router.get("/{author_id}")
async def get_one_author(author_id: int) -> ViewAuthor:
    return await AuthorService.find_one_object_by_id(author_id)


@router.post("/add_author")
async def create_author(author: CreateAuthor):
    return await AuthorService.create_object(author)


@router.put("/{author_id}")
async def update_author(author_id: int, author: CreateAuthor):
    return await AuthorService.update_object(author_id, author)


@router.delete("/{author_id}")
async def delete_author(author_id: int):
    return await AuthorService.delete_object(author_id)
