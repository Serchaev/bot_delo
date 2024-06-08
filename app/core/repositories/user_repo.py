from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import User


class UserRepo:

    @classmethod
    async def add_user(
        cls,
        session: AsyncSession,
        tg_id: str,
        username: str | None,
        first_name: str | None,
        last_name: str | None,
    ):
        query = insert(User).values(tg_id=tg_id, username=username, first_name=first_name, last_name=last_name)
        await session.execute(query)
        await session.commit()

    @classmethod
    async def get_user(cls, session: AsyncSession, tg_id: str) -> User:
        query = select(User).where(User.tg_id == tg_id)
        result = await session.execute(query)
        return result.scalars().first()

    @classmethod
    async def update_user(
        cls,
        session: AsyncSession,
        tg_id: str,
        username: str | None,
        first_name: str | None,
        last_name: str | None,
    ):
        query = (
            update(User)
            .values(username=username, first_name=first_name, last_name=last_name)
            .where(User.tg_id == tg_id)
        )
        await session.execute(query)
        await session.commit()
