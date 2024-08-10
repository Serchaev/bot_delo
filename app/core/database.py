from asyncio import current_task

from sqlalchemy.ext.asyncio import async_scoped_session, async_sessionmaker, create_async_engine

from app.core.settings import settings


class DatabaseFactory:
    def __init__(
        self,
        db_url: str,
        db_echo: bool = False,
    ):
        self.engine = create_async_engine(
            url=db_url,
            echo=db_echo,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
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
)
