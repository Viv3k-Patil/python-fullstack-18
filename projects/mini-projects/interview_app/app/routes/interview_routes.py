import datetime

from fastapi import APIRouter
from app.schemas.interview_request import InterviewCreateRequest, InterviewUpdateRequest
<<<<<<< HEAD
<<<<<<< HEAD
from app.services import interview_services
=======
from app.services import interview_service
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
from app.services import interview_service
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
from app.schemas.interview_response import InterviewResponse
router = APIRouter(prefix="/interviews")


# create interview
@router.post("/")
def create_interview(request: InterviewCreateRequest):
    # request is pJSON which deserializaed to python object
    # python object send to service
    # service returns python dict
<<<<<<< HEAD
<<<<<<< HEAD
    data = interview_services.create_interview(request)
=======
    data = interview_service.create_interview(request)
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
    data = interview_service.create_interview(request)
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06

    # need to convert python dict to pydantic object of InterviewResponse
    response = InterviewResponse(**data)
    return response


# get all interviews
@router.get("/")
def get_all_interviews():
<<<<<<< HEAD
<<<<<<< HEAD
    interview_list = interview_services.get_all_interviews()
=======
    interview_list = interview_service.get_all_interviews()
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
    interview_list = interview_service.get_all_interviews()
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
    response_list = []
    for interview_python_dict in interview_list:
        pydantic_obj = InterviewResponse(**interview_python_dict)
        response_list.append(pydantic_obj)
    return interview_list

# get interview by time ( start_time and end_time)
@router.get("/by-time")
def get_interview_by_time(start_time: datetime.datetime, end_time: datetime.datetime):
<<<<<<< HEAD
<<<<<<< HEAD
    output_list = interview_services.get_interview_by_time(start_time,end_time)
=======
    output_list = interview_service.get_interview_by_time(start_time,end_time)
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
    output_list = interview_service.get_interview_by_time(start_time,end_time)
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
    response_list = []
    for each_interview in output_list:
        py_obj = InterviewResponse(**each_interview)
        response_list.append(py_obj)
    return response_list

# get interview by id
@router.get("/{interview_id}")
def get_interview_by_id(interview_id: int):
<<<<<<< HEAD
<<<<<<< HEAD
    ret_interview = interview_services.get_interview_by_id(interview_id)
=======
    ret_interview = interview_service.get_interview_by_id(interview_id)
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
    ret_interview = interview_service.get_interview_by_id(interview_id)
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
    response_obj = InterviewResponse(**ret_interview)
    return response_obj


# update interview by id
@router.put("/{interview_id}")
def update_interview_by_id(interview_id: int, request: InterviewUpdateRequest):
<<<<<<< HEAD
<<<<<<< HEAD
    updated_interview = interview_services.update_interview_by_id(interview_id, request)
=======
    updated_interview = interview_service.update_interview_by_id(interview_id, request)
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
    updated_interview = interview_service.update_interview_by_id(interview_id, request)
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
    response_obj = InterviewResponse(**updated_interview)
    return response_obj


# delete interview by id
@router.delete("/{interview_id}")
def delete_interview_by_id(interview_id: int):
<<<<<<< HEAD
<<<<<<< HEAD
    is_interview_deleted =  interview_services.delete_interview(interview_id)
=======
    is_interview_deleted =  interview_service.delete_interview(interview_id)
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
    is_interview_deleted =  interview_service.delete_interview(interview_id)
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
    return {
        "status": f"Interview delete response: {is_interview_deleted}"
    }

<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======

>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
