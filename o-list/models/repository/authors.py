from typing import Annotated

from core.database import get_db_connection
from fastapi import Depends
from models.entities.authors import Author
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


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

    async def get_by_name(self, name: str | None = None) -> Author:
        """Get author by name"""
        return await self.session.scalar(select(Author).where(Author.name == name))
