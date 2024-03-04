from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base SQLAlchemy Model"""

    pass


from .authors import Author
from .books import Book
