from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import hash_password


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(
        self,
        db: Session,
        user_create: UserCreate,
    ) -> User:

        existing = self.repository.get_by_email(
            db,
            user_create.email,
        )

        if existing:
            raise ValueError("Email already exists.")

        user = User(
            email=user_create.email,
            username=user_create.username,
            hashed_password=hash_password(
                user_create.password
            ),
        )

        self.repository.create(db, user)

        db.commit()

        return user

    def get_users(self, db: Session):
        return self.repository.get_all(db)


