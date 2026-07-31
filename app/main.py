from fastapi import FastAPI

from app.core.config import settings
from app.api.router import api_router

from app.api.exception_handler import app_exception_handler
from app.core.exceptions import AppException
from app.core.logging import setup_logging
from app.middleware.request_id import RequestIDMiddleware
from app.middleware.logging import LoggingMiddleware


setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)
app.add_middleware(RequestIDMiddleware)
app.add_middleware(LoggingMiddleware)
app.add_exception_handler(
    AppException,
    app_exception_handler,
)
app.include_router(api_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "debug": settings.DEBUG,
    }