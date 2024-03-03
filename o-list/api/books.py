# from typing import Annotated
# from typing import Union

# from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException


router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/")
async def create_book(
    request: ...,
) -> None:
    """Create book registers in database"""
    try:
        return await ...
    except Exception:
        raise HTTPException(500, detail="")
