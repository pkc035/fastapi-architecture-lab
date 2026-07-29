from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base


class User(Base):

    __tablename__ = "users"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )


    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
    )


    username: Mapped[str] = mapped_column(
        String(50)
    )