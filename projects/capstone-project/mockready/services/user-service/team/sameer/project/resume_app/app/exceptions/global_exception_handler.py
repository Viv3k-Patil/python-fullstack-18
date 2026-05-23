from fastapi.responses import JSONResponse
from fastapi import Request
from app.exceptions.custom_exception import ResumeAppException


def global_exception_handler(app):

    @app.exception_handler(ResumeAppException)
    async def handle_app_exception(request: Request, exc: ResumeAppException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message}
        )

    @app.exception_handler(Exception)
    async def handle_unknown(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content={"detail": "Internal server error."})