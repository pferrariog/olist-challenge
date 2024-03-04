from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from . import Base
from .authors import Author


class Book(Base):
    """Book's default model"""

    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    edition: Mapped[int]
    publication_year: Mapped[int]
    authors: Mapped[list[Author]] = relationship("Author")
