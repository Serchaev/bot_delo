from app.core.database import db_factory
from app.core.repositories.refer_repo import ReferRepo


class ReferService:

    @classmethod
    async def get_count_children(cls, tg_id: str):
        async with db_factory.session_factory() as session:
            count = await ReferRepo.get_count_children(session=session, tg_id=tg_id)
            return count[0]
