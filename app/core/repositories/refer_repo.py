from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import count

from app.core.models import Refer


class ReferRepo:

    @classmethod
    async def add_refer(cls, session: AsyncSession, added: str, adding: str):
        query = insert(Refer).values(added=added, adding=adding)
        await session.execute(query)
        await session.commit()

    @classmethod
    async def get_count_children(cls, session: AsyncSession, tg_id: str):
        query = select(count()).select_from(Refer).where(Refer.adding == tg_id)
        result = await session.execute(query)
        return result.fetchone()
