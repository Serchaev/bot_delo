from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import Base


class User(Base):
    __tablename__ = "user_test"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
