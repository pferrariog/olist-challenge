from typing import AsyncGenerator

from core.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine(settings.DATABASE_URL)


async def get_db_connection() -> AsyncGenerator:
    """Generate a database session"""
    async with AsyncSession(autocommit=False, autoflush=False, bind=engine) as session:
        yield session
