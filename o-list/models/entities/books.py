from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base SQLAlchemy Model"""

    pass


class Book(DeclarativeBase):
    """Book's default model"""

    __tablename__ = "book"
