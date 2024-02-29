from sqlalchemy import select
from sqlalchemy.orm import Session

from ..entities.authors import Author


class AuthorRepository:
    """Manage Author's table operations"""

    def __init__(self, session: Session) -> None:
        """Class initializer method"""
        self.session = session

    def get_all(self) -> list[Author]:
        """Get all registers from database"""
        return self.session.scalars(select(Author)).all()

    def get_by_id(self) -> Author:
        """Get register by id"""
