from app.core.database import db_factory
from app.core.repositories.consultation_repo import ConsultationRepo


class ConsultationService:

    @staticmethod
    async def add_consultation(
        phone_number: str,
        first_name: str,
        last_name: str | None,
        tg_id: str,
    ):
        async with db_factory.session_factory() as session:
            await ConsultationRepo.add_consultation(
                session=session,
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                tg_id=tg_id,
            )
