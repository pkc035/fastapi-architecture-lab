import time

from app.core.logging import logger
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next,
    ):
        start = time.time()
        response = await call_next(request)
        elapsed = (
            time.time()
            - start
        )
        logger.info(
            "%s %s %s %.3fs",
            request.method,
            request.url.path,
            response.status_code,
            elapsed,
        )

        return response