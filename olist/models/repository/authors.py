from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.database import get_db_connection
from ..entities.authors import Author


class AuthorRepository:
    """Manage Author's table operations"""

    def __init__(self, session: Annotated[AsyncSession, Depends(get_db_connection)]) -> None:
        """Class initializer method"""
        self.session = session

    async def get_all_paginated(self, page: int | None = None) -> list[Author]:
        """Get all registers from database"""
        query = await select(Author).limit(10)
        if page:
            query = await query.offset(page * 10)

        return await self.session.scalars(query).all()

    async def get_by_name(self, name: str) -> Author | None:
        """Get author by name"""
        return await self.session.scalar(select(Author).where(Author.name == name))

    async def get_by_id(self, id: int) -> Author | None:
        """Get author by id"""
        return await self.session.scalar(select(Author).where(Author.id == id))
