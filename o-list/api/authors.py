from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from ..models.repository.authors import AuthorRepository


router = APIRouter("/authors", tags=["Authors"])


@router.get("/")
def get_authors(repo: Annotated[AuthorRepository, Depends()], name: str | None = None, page: int | None = None) -> ...:
    """Get authors from database"""
    if name:
        author = repo.get_by_name(name)
        if not author:
            raise ...

    return repo.get_all_paginated(page)
