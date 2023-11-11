# fastapi_library

REST API online library service implemented on fastapi. The service allows you to add books to the main database using an API.

![library](https://github.com/IgorBekchruin/fastapi_library/assets/107909070/647ce5c6-6094-4b1a-a25d-ddeaff2b6957)

Backend:
* Python
* Fastapi
* SQLAlchemy
* Alembic

DB:
* PostgreSQL

Tools:
* Redis

Frontend:
* TailwindCSS

API service for uploading books to a common database. Models for author, genres and books have been implemented. For more complete information about the book, the ability to download the cover of the book, which is issued in the "webp" format, has been added.
In the "dev" branch, the project is compiled into docker and docker compose.
To view the service, a frontend has been implemented on the TailwindCSS framework.
