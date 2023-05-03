from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from src.db.database import Base


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), unique=True)

    def __repr__(self):
        return f"Жанр: {self.name}"


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50))
    birthday = Column(Date)
    description = Column(String(500))


    def __repr__(self):
        return f"<Автор: {self.name}>"

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50))
    created_at = Column(Date)
    text = Column(String(300))
    book_id = Column(ForeignKey('book.id'))
    book = relationship("Book", back_populates='comment')

    def __repr__(self):
        return f"Комментарий от {self.name}"


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), unique=True)
    data = Column(Date)
    annotate = Column(String(500))
    comment = relationship('Comment', back_populates='book')

    author_id = Column(ForeignKey('author.id'))
    author = relationship('Author', backref='author',  uselist=False)

    genre_id = Column(ForeignKey('genre.id'))
    genre = relationship('Genre', backref='genre',  uselist=False)

    # picture = image_attachment('BookPicture')

    def __repr__(self):
        return f"Книга: {self.name}"


# class BookPicture(Base, Image):
#     __tablename__ = 'book_picture'
#
#     book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
#     book = relationship('Book')