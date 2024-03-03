from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///database.db")


def get_db_connection() -> Generator:
    """Generate a database session"""
    with Session(autocommit=False, autoflush=False, bind=engine) as session:
        yield session
