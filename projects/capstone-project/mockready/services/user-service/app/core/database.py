from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from sqlalchemy.orm import DeclarativeBase
from app.core.settings import get_settings

settings = get_settings()
# connection factory
engine = create_async_engine(
    settings.database_url,
    pool_size = 5,
    pool_pre_ping = True,
    echo=settings.is_development
)
# base declaration
class Base(DeclarativeBase):
    pass

# session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_= AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit = False
)

async def get_db()-> AsyncSessionLocal:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
