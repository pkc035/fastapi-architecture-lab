from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import get_db
from app.schemas.auth import LoginRequest
from app.schemas.auth import TokenResponse
from app.services.auth_service import AuthService


router = APIRouter()


service = AuthService()



@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    token = service.login(
        db=db,
        email=form_data.username,
        password=form_data.password,
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }