from entities import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Author(Base):
    """Author's default model"""

    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def __repr__(self) -> str:
        """Return an object representation"""
        return f"Author({self.id=}, {self.name=})"
