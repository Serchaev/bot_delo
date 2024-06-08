from asyncpg import UniqueViolationError
from sqlalchemy.exc import IntegrityError

from app.core.database import db_factory
from app.core.repositories.refer_repo import ReferRepo
from app.core.repositories.user_repo import UserRepo


class UserService:

    @classmethod
    async def add_user(
        cls,
        tg_id: str,
        username: str | None,
        first_name: str | None,
        last_name: str | None,
        refer_id: str | None,
    ):
        async with db_factory.session_factory() as session:
            user = await UserRepo.get_user(session=session, tg_id=tg_id)
            if not user:
                await UserRepo.add_user(
                    session=session,
                    tg_id=tg_id,
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                )
                if refer_id is not None:
                    if refer_id:
                        await ReferRepo.add_refer(session=session, adding=refer_id, added=tg_id)
            else:
                await UserRepo.update_user(
                    session=session,
                    tg_id=tg_id,
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                )
