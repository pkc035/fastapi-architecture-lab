from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AppException



async def app_exception_handler(
    request: Request,
    exc: AppException,
):
    request_id = getattr(
        request.state,
        "request_id",
        None,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "code": exc.code,
            "message": exc.message,
            "request_id": request_id,
        },

    )