from datetime import datetime, timezone

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import Base


class Refer(Base):
    __tablename__ = "referrals"

    id: Mapped[int] = mapped_column(primary_key=True)
    adding: Mapped[str] = mapped_column(index=True)
    added: Mapped[str] = mapped_column(index=True)
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
