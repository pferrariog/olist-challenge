from typing import Annotated
from typing import Union

from fastapi import APIRouter
from fastapi import Depends

from ..models.repository.books import BookRepository
from ..schemas import BookCompleteSchema
from ..schemas import BookOptional
from ..schemas import BookSchema


router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/")
async def create_book(request: BookSchema, repo: Annotated[BookRepository, Depends()]) -> Union[BookSchema, None]:
    """Create book register in database"""
    return await repo.create_book(**request)


@router.get("/{id}")
async def get_book(
    id: int, repo: Annotated[BookRepository, Depends()], all: bool = False
) -> Union[BookSchema, BookCompleteSchema, None]:
    """Get book register by id"""
    if all:
        return await BookCompleteSchema(**repo.get_by_id(id))
    return await BookSchema(**repo.get_by_id(id))


@router.patch("/{id}")
async def update_book(
    id: int,
    update_fields: BookOptional,
    repo: Annotated[BookRepository, Depends()],
) -> Union[BookSchema, None]:
    """Update book register by id with given values"""
    return await repo.update_book(id, update_fields)


@router.get("/{id}")
async def delete_book(
    id: int,
    repo: Annotated[BookRepository, Depends()],
) -> None:
    """Delete book register by id"""
    return await repo.delete_by_id(id)
