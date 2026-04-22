import datetime

from fastapi import APIRouter
from app.schemas.interview_request import InterviewCreateRequest, InterviewUpdateRequest
from app.services import interview_service
from app.schemas.interview_response import InterviewResponse
router = APIRouter(prefix="/interviews")


# create interview
@router.post("/")
def create_interview(request: InterviewCreateRequest):
    # request is pJSON which deserializaed to python object
    # python object send to service
    # service returns python dict
    data = interview_service.create_interview(request)

    # need to convert python dict to pydantic object of InterviewResponse
    response = InterviewResponse(**data)
    return response


# get all interviews
@router.get("/")
def get_all_interviews():
    interview_list = interview_service.get_all_interviews()
    response_list = []
    for interview_python_dict in interview_list:
        pydantic_obj = InterviewResponse(**interview_python_dict)
        response_list.append(pydantic_obj)
    return interview_list

# get interview by time ( start_time and end_time)
@router.get("/by-time")
def get_interview_by_time(start_time: datetime.datetime, end_time: datetime.datetime):
    output_list = interview_service.get_interview_by_time(start_time,end_time)
    response_list = []
    for each_interview in output_list:
        py_obj = InterviewResponse(**each_interview)
        response_list.append(py_obj)
    return response_list

# get interview by id
@router.get("/{interview_id}")
def get_interview_by_id(interview_id: int):
    ret_interview = interview_service.get_interview_by_id(interview_id)
    response_obj = InterviewResponse(**ret_interview)
    return response_obj


# update interview by id
@router.put("/{interview_id}")
def update_interview_by_id(interview_id: int, request: InterviewUpdateRequest):
    updated_interview = interview_service.update_interview_by_id(interview_id, request)
    response_obj = InterviewResponse(**updated_interview)
    return response_obj


# delete interview by id
@router.delete("/{interview_id}")
def delete_interview_by_id(interview_id: int):
    is_interview_deleted =  interview_service.delete_interview(interview_id)
    return {
        "status": f"Interview delete response: {is_interview_deleted}"
    }


