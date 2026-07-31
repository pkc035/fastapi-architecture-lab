from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def create(self, db: Session, user: User) -> User:
        db.add(user)
        db.flush()      # INSERT 수행 (commit은 아님)
        db.refresh(user)
        return user

    def get_by_email(self, db: Session, email: str) -> User | None:
        stmt = select(User).where(User.email == email)

        result = db.execute(stmt)

        return result.scalar_one_or_none()

    def get_all(self, db: Session) -> list[User]:
        stmt = select(User)

        result = db.execute(stmt)

        return list(result.scalars().all())

    def get_by_id(
        self,
        db: Session,
        user_id: int,
    ):

        stmt = select(User).where(
            User.id == user_id
        )

        result = db.execute(stmt)

        return result.scalar_one_or_none()