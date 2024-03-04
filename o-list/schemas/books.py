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
