from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.author.models import Author
    from src.genre.models import Genre


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    data: Mapped[date]
    annotate: Mapped[str] = mapped_column(String(1000))
    image: Mapped[str]

    author_id: Mapped[int] = mapped_column(
        ForeignKey("author.id", ondelete="SET NULL"), nullable=True
    )
    author: Mapped["Author"] = relationship(
        "Author", back_populates="book", lazy="joined"
    )

    genre_id: Mapped[int] = mapped_column(
        ForeignKey("genre.id", ondelete="SET NULL"), nullable=True
    )
    genre: Mapped["Genre"] = relationship("Genre", back_populates="book", lazy="joined")

    pages: Mapped[int]
    rating: Mapped[float] = mapped_column(nullable=True)

    def __repr__(self):
        return f"Книга: {self.name}"
