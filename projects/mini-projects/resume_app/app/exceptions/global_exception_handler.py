from fastapi.responses import JSONResponse
from fastapi import Request
<<<<<<< HEAD
<<<<<<< HEAD
from app.exceptions.custom_exceptions import ResumeAppException
=======
from app.exceptions.custom_exception import ResumeAppException
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
from app.exceptions.custom_exception import ResumeAppException
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06


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