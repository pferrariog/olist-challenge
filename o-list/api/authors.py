from typing import Annotated
from typing import Union

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from models.repository.authors import AuthorRepository
from schemas import AuthorSchema
from schemas import AuthorsListSchema


router = APIRouter(prefix="/authors", tags=["Authors"])

# TODO add async requests


@router.get("/")
def get_authors(
    repo: Annotated[AuthorRepository, Depends()], name: str | None = None, page: int | None = None
) -> Union[AuthorSchema, AuthorsListSchema, None]:
    """Get authors from database"""
    if name:
        author = repo.get_by_name(name)
        if not author:
            raise HTTPException(404, "Author not found")

    return repo.get_all_paginated(page)
