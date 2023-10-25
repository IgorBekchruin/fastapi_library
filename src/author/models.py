from typing import TYPE_CHECKING
from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.book.models import Book


class Author(Base):
    __tablename__ = 'author'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    book: Mapped["Book"] = relationship(back_populates='author', lazy='joined')
    # birthday: Mapped[Date]
    # description: Mapped[str] = mapped_column(String(250))


    def __repr__(self):
        return f"<Автор: {self.name}>"

