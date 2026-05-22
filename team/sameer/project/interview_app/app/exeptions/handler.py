from fastapi import Request
from app.exeptions.custom_exception import InterviewNotFoundException   


def global_exception_handler(app):
    @app.exception_handler(InterviewNotFoundException)
    def interview_not_found_exception_handler(ex: Exception , request: Request ):
        return {
            "error": f"Interview with id {ex.interview_id} not found."
            }
      
 
    @app.exception_handler(Exception)
    def generic_exception_handler(ex: Exception, request: Request):
         return {
             "error": "An unexpected error occurred."
         }  