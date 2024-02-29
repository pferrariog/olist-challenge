from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from ..services.authors import Service


router = APIRouter("/authors", tags=["Authors"])


router.get("/")


def get_authors(service: Annotated[Service, Depends()]) -> ...:
    """Get all authors from database"""
    authors = service.get_all()
    return authors
