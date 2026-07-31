from fastapi import APIRouter

from app.api.v1.users import router as user_router
from app.api.v1.auth import router as auth_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    user_router,
    prefix="/users",
    tags=["Users"],
)

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"],
)