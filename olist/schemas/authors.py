from pydantic import BaseModel


class AuthorSchema(BaseModel):
    """Author's endpoint base response"""

    id: int
    name: str


class AuthorsListSchema(BaseModel):
    """List of Author's base response for get all request"""

    authors: list[AuthorSchema]
