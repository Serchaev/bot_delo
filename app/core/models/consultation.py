from datetime import datetime, timezone

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import Base


class Consultation(Base):
    __tablename__ = "consultations"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone_number: Mapped[str]
    tg_id: Mapped[str] = mapped_column(index=True)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    date_created = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    date_updated = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=lambda: datetime.now(timezone.utc).astimezone(),
    )
