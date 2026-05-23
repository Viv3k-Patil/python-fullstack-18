from urllib import response

from fastapi import APIRouter
from app.schemas.interview_request import InterviewCreateRequest
from app.services import interview_services
from app.schemas.interview_responce import InterviewResponse
import datetime 
router = APIRouter(prefix="/interviews")


# create interview
@router.post("/")
def create_interview(request: InterviewCreateRequest):
    # data is python dict
    data = interview_services.create_interview(request)
    # data is python dict but we want to return pydantic model
    return InterviewResponse(**data)    


# get all interviews
@router.get("/")
def get_all_interviews():
    interview_list = interview_services.get_all_interviews()
    response_list = []
    for interview in interview_list:        
        pydantic_obj = InterviewResponse(**interview)
        response_list.append(pydantic_obj)
    return interview_list


# get interview by id
@router.get("/{interview_id}")
def get_interview_by_id(interview_id: int):
    interview = interview_services.get_interview_by_id(interview_id)
    return InterviewResponse(**interview)


# update interview by id
@router.put("/{interview_id}")
def update_interview_by_id(interview_id: int):
    updated_interview = interview_services.update_interview_by_id(interview_id)
    return InterviewResponse(**updated_interview)


# delete interview by id
@router.delete("/{interview_id}")
def delete_interview_by_id(interview_id: int):
    interview_deleted =  interview_services.delete_interview_by_id(interview_id)
    return interview_deleted


# get interview by time ( start_time and end_time)
@router.get("/by-time")
def get_interview_by_time(start_time: str, end_time: str):
    output_list = interview_services.get_interview_by_time(start_time, end_time)
    return [InterviewResponse(**interview) for interview in output_list]    