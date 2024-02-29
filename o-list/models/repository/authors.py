from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from ...core.database import get_db_connection
from ..entities.authors import Author


class AuthorRepository:
    """Manage Author's table operations"""

    def __init__(self, session: Annotated[Session, Depends(get_db_connection)]) -> None:
        """Class initializer method"""
        self.session = session

    def get_all_paginated(self, page: int | None = None) -> list[Author]:
        """Get all registers from database"""
        query = select(Author).limit(10)
        if page:
            query = query.offset(page * 10)

        return self.session.scalars(query).all()

    def get_by_name(self, name: str | None = None) -> Author:
        """Get author by name"""
        return self.session.scalar(select(Author).where(Author.name == name))
