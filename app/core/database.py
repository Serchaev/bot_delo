from asyncio import current_task
from datetime import datetime

# from redis import asyncio as aioredis
from sqlalchemy import NullPool, create_engine, func
from sqlalchemy.ext.asyncio import (
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
    sessionmaker,
)

from app.core.settings import settings

if settings.MODE == "TEST":
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_PARAMS = {}


class DatabaseFactory:
    def __init__(
        self,
        db_url: str,
        db_sync_url: str,
        db_echo: bool = False,
    ):
        self.engine = create_async_engine(
            url=db_url,
            echo=db_echo,
            **DATABASE_PARAMS,
        )
        self.sync_engine = create_engine(
            url=db_sync_url,
            echo=db_echo,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

        self.sync_session_factory = sessionmaker(
            bind=self.sync_engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_depends(self):
        async with self.session_factory() as session:
            yield session
            await session.close()


db_factory = DatabaseFactory(
    db_url=settings.db_url,
    db_sync_url=settings.db_sync_url,
    db_echo=settings.db_echo,
)
