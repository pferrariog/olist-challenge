from typing import Annotated

from core.database import get_db_connection
from fastapi import Depends
from models.entities.books import Book
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BookRepository:
    """Manage Book's table operations"""

    def __init__(self, session: Annotated[AsyncSession, Depends(get_db_connection)]) -> None:
        """Class initializer method"""
        self.session = session

    async def create_book(self, name: str, edition: int, publication_year: int, authors: list) -> Book:
        """Create book register in database"""

        book = Book(name, edition, publication_year, authors)

        self.session.add(book)
        await self.session.commit()

        return book

    async def get_by_id(self, id: int) -> Book | None:
        """Get book register by given id"""
        return self.session.scalar(select(Book).where(Book.id == id))

    async def update_book(self, **kw) -> Book | None:
        """Update fields in a book register"""

    async def delete_by_id(self, id: int) -> None:
        """Delete a book register from database"""

        book = self.get_by_id(id)
        if not book:
            raise ...

        self.session.delete(book)
        await self.session.commit()
