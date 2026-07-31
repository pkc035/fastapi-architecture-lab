from app.core.errors import ErrorCode


class AppException(Exception):

    def __init__(
        self,
        code: ErrorCode,
        message: str,
        status_code: int,
    ):

        self.code = code
        self.message = message
        self.status_code = status_code



class NotFoundException(AppException):

    def __init__(
        self,
        code: ErrorCode,
        message="Resource not found",
    ):

        super().__init__(
            code,
            message,
            404,
        )



class ConflictException(AppException):

    def __init__(
        self,
        code: ErrorCode,
        message="Conflict",
    ):

        super().__init__(
            code,
            message,
            409,
        )



class UnauthorizedException(AppException):

    def __init__(
        self,
        code: ErrorCode,
        message="Unauthorized",
    ):

        super().__init__(
            code,
            message,
            401,
        )