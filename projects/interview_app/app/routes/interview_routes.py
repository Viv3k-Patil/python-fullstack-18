from fastapi import APIRouter
from app.schemas.interview_request import InterviewCreateRequest
from app.db.interview_db import interviews
router=APIRouter(prefix="/Interview")

#Create  POST interview
@router.post("/")
def create_interview(request:InterviewCreateRequest):   
  pass
  
    
#Create GET interview
@router.get("/")
def show_interviews():
   pass

#GET interview by id
@router.get("/{interview_id}")
def get_interview_by_id(interview_id:int):
    pass
   
#Create PUT / UPDTE interview
@router.put("/{interview_id}")
def update_interview(interview_id:int):
    pass

# DELET interview by id
@router.delete("/{interview_id}")
def delete_interviwe_by_id(interview_id:int):
    pass

#get DATE AND TIME interviewm{time=IST,Date=int}
@router.get("/by-time")
def get_time(start_time:str,end_time:str):
    pass

