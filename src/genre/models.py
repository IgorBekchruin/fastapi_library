from typing import TYPE_CHECKING
from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.book.models import Book

class Genre(Base):
    __tablename__ = 'genre'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    book: Mapped["Book"] = relationship(back_populates='genre', lazy='joined')

    def __repr__(self):
        return f"Жанр: {self.name}"
