from typing import Optional

from pydantic import BaseModel


class BookSchema(BaseModel):
    """Book's endpoint base response"""

    name: str
    edition: int
    publication_year: int
    authors: list[int]


class BookCompleteSchema(BookSchema):
    """Book's endpoint complete fields"""

    id: int


class BookOptional(BookSchema):
    """Book's endpoint optional schema"""

    __annotations__ = {key: Optional[value] for key, value in BookSchema.__annotations__.items()}
