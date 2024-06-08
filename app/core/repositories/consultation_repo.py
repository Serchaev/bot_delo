from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import Consultation


class ConsultationRepo:

    @staticmethod
    async def add_consultation(
        session: AsyncSession,
        phone_number: str,
        first_name: str,
        last_name: str | None,
        tg_id: str,
    ):
        query = insert(Consultation).values(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            tg_id=tg_id,
        )
        await session.execute(query)
        await session.commit()
