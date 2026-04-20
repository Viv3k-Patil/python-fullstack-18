from fastapi import Request
from app.exceptions.custom_exceptions import InterviewNotFoundException

def global_exception_handler(app):

    @app.exception_handler(InterviewNotFoundException)
    def handle_interview_not_found_exceptipn(ex: Exception, request: Request):
        return {
            "status": f"the error is {ex}"
        }
    
    @app.exception_handler(Exception)
    def handling_generic_exception(ex: Exception, request: Request):
        return {
            "status": f"the error is {ex}"
        }