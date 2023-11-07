from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from src.book.schemas import CreateBook, ViewBook
from src.book.service import BookService

router = APIRouter(prefix="/book", tags=["Book"])


@router.get("/")
@cache(expire=60 * 3)
async def get_list_books() -> list[ViewBook]:
    return await BookService.find_all_objects(20)


@router.get("/{book_id}")
async def get_newlist_books(book_id: int) -> ViewBook:
    return await BookService.find_one_object_by_id(book_id)


@router.post("/add_book")
async def create_book(book: CreateBook = Depends()):
    return await BookService.add_new_book(book)


@router.put("/{book_id}")
async def update_book(book_id: int, book: CreateBook):
    return await BookService.update_object(book_id, book)


@router.delete("/{book_id}")
async def delete_book(book_id: int):
    return await BookService.delete_object(book_id)
