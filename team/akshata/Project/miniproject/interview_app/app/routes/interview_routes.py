
from fastapi import APIRouter
from app.schemas.interview_request import interviewCreateRequest
from datetime import datetime


router = APIRouter(prefix="/interviews")

# create interview
@router.post("/")
def create_interview():
    pass

# get all interviews
@router.get("/")
def get_all_interview():
    pass

#get interview by id
@router.get("/{interview_id}")
def get_inteview_by_id(interview_id : int):
    pass

# update interview by id
@router.post("/{interview_id}")
def update_interview_by_id(interview_id : int):
    pass


# delete interview by id
@router.delete("/{interview_id}")
def delete_interview_by_id(interview_id : int):
    pass

#get interview by time(start_tie and end_time)
@router.get("/by_time")
def get_interview_by_time(start_time :str , end_time : str):
    pass









