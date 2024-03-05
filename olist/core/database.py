from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from .settings import settings


engine = create_async_engine(settings.DATABASE_URL)


async def get_db_connection() -> AsyncGenerator:
    """Generate a database session"""
    async with AsyncSession(autocommit=False, autoflush=False, bind=engine) as session:
        yield session
