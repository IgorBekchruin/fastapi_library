from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from src.author.service import AuthorService
from src.book.service import BookService
from src.genre.service import GenreService

page_router = APIRouter(prefix="/library", tags=["library"])

templates = Jinja2Templates(directory="src/templates")


@page_router.get("/")
async def main_page(request: Request):
    new_books = await BookService.find_all_objects()
    pop_books = await BookService.find_all_objects()
    return templates.TemplateResponse(
        "main.html",
        {"request": request, "new_books": new_books, "pop_books": pop_books},
    )


@page_router.get("/newbook")
async def get_books(request: Request):
    book_list = await BookService.find_all_objects(18)
    return templates.TemplateResponse(
        "newbook.html", {"request": request, "book_list": book_list}
    )


@page_router.get("/popularbook")
async def get_pop_books(request: Request):
    pop_book_list = await BookService.find_all_objects(18)
    return templates.TemplateResponse(
        "popular.html", {"request": request, "pop_book_list": pop_book_list}
    )


@page_router.get("/book/{book_name}")
async def get_detail_book(book_name: str, request: Request):
    book = await BookService.find_detail_book(book_name)
    return templates.TemplateResponse(
        "bookdetail.html", {"request": request, "book": book}
    )


# @page_router.post('/book/createcomment')
# async def createcomment(
#         request: Request,
#         book_name: str,
#         name: str = Form(),
#         text: str = Form(),
#         session: AsyncSession = Depends(get_async_session)
# ):
#     comment = {
#         'name': name,
#         'text': text,
#     }
#     statement = insert(Comment).values(**comment)
#     await session.execute(statement)
#     await session.commit()
#     return comment


@page_router.get("/authors")
async def get_authors(request: Request):
    author_list = await AuthorService.find_all_objects_for_pages()
    return templates.TemplateResponse(
        "author.html", {"request": request, "author_list": author_list}
    )


@page_router.get("/authors/{author_id}")
async def get_books_by_author(author_id: int, request: Request):
    author_dict = {"author_id": author_id}
    books = await BookService.find_books_by_filter(author_dict)
    return templates.TemplateResponse(
        "books_by_author.html", {"request": request, "books": books}
    )


@page_router.get("/genres")
async def get_genres(request: Request):
    genre_list = await GenreService.find_all_objects_for_pages()
    return templates.TemplateResponse(
        "genre.html", {"request": request, "genre_list": genre_list}
    )


@page_router.get("/genres/{genre_id}")
async def get_books_by_genre(genre_id: int, request: Request):
    genre_dict = {"genre_id": genre_id}
    books = await BookService.find_books_by_filter(genre_dict)
    return templates.TemplateResponse(
        "books_by_genre.html", {"request": request, "books": books}
    )


@page_router.get("/about")
def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@page_router.get("/contact")
def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})
