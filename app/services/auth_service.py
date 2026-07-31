from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.core.security import create_access_token
from app.repositories.user_repository import UserRepository
from app.core.exceptions import UnauthorizedException
from app.core.errors import ErrorCode


class AuthService:


    def __init__(self):

        self.repository = UserRepository()



    def login(
        self,
        db: Session,
        email: str,
        password: str,
    ):

        user = self.repository.get_by_email(
            db,
            email,
        )


        if not user:
            raise UnauthorizedException(
                ErrorCode.UNAUTHORIZED,
                "Invalid credentials",
            )


        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise UnauthorizedException(
                ErrorCode.UNAUTHORIZED,
                "Invalid credentials",
            )


        token = create_access_token(
            {
                "sub": str(user.id)
            }
        )


        return token