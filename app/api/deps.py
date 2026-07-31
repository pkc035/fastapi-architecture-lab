from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session


from app.core.security import oauth2_scheme
from app.core.security import decode_access_token
from app.core.exceptions import UnauthorizedException, NotFoundException
from app.core.errors import ErrorCode
from app.repositories.user_repository import UserRepository

from app.db.session import SessionLocal



def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    if not token:
        raise UnauthorizedException(
            ErrorCode.UNAUTHORIZED,
            "Authentication required",
        )
    
    payload = decode_access_token(token)

    if payload is None:
        raise UnauthorizedException(
            ErrorCode.UNAUTHORIZED,
            "Authentication required",
        )


    user_id = payload.get("sub")

    if user_id is None:
        raise NotFoundException(
            "User not found"
        )

    repository = UserRepository()
    user = repository.get_by_id(
        db,
        int(user_id),
    )

    if user is None:
        raise NotFoundException(
            "User not found"
        )

    return user