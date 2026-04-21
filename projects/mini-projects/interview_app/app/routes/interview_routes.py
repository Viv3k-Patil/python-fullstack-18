from fastapi import APIRouter
from app.schemas.interview_request import InterviewCreateRequest
from app.services import interview_service
from app.schemas.interview_response import InterviewResponse
router = APIRouter(prefix="/interviews")


# create interview
@router.post("/")
def create_interview(request: InterviewCreateRequest):
    # data is python dict
    data = interview_service.create_interview(request)
    return data


# get all interviews
@router.get("/")
def get_all_interviews():
    interview_list = interview_service.get_all_interviews()
    return interview_list


# get interview by id
@router.get("/{interview_id}")
def get_interview_by_id(interview_id: int):
    ret_interview = interview_service.get_interview_by_id()
    return ret_interview


# update interview by id
@router.put("/{interview_id}")
def update_interview_by_id(interview_id: int):
    updated_interview = interview_service.update_interview_by_id()
    return updated_interview


# delete interview by id
@router.delete("/{interview_id}")
def delete_interview_by_id(interview_id: int):
    is_interview_deleted =  interview_service.delete_interview_by_id()
    return is_interview_deleted


# get interview by time ( start_time and end_time)
@router.get("/by-time")
def get_interview_by_time(start_time: str, end_time: str):
    output_list = interview_service.get_interview_by_time()
    return output_list