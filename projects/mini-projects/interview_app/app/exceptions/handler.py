from fastapi import Request
from fastapi.responses import JSONResponse
<<<<<<< HEAD
<<<<<<< HEAD
from app.exceptions.custom_exception import InterviewNotFoundException
=======
from app.exceptions.custom_exceptions import InterviewNotFoundException
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
from app.exceptions.custom_exceptions import InterviewNotFoundException
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06

def global_exception_handler(app):

    @app.exception_handler(InterviewNotFoundException)
    def handle_interview_not_found_exceptipn(request: Request, ex: InterviewNotFoundException):
        return JSONResponse(
            status_code= 400,
            content={
<<<<<<< HEAD
<<<<<<< HEAD
                "message" : ex.msg   
=======
                "message" : ex.msg
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
                "message" : ex.msg
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
            }
        )
    
    # @app.exception_handler(NameError)
    # def handle_name_error(request: Request, ex:NameError ){

    # }

    @app.exception_handler(Exception)
    def handling_generic_exception(ex: Exception, request: Request):
        return JSONResponse(
            status_code= 401,
            content={
                "status":"hey there"
            }
<<<<<<< HEAD
<<<<<<< HEAD
        )
        
=======
        )
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
        )
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
