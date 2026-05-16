from fastapi import APIRouter  # instead of using @app im importing APIRouter
from app.schemas.interview_request import InterviewCreateRequest, InterviewUpdateRequest




#creating a object for APIRouter
router = APIRouter(prefix="/interviews")

#create interview
@router.post("/")
def create_interview(request: InterviewCreateRequest):
     data = interview_service.create_interview(request)
     response = InterviewResponse(**data)
     return response


#get all interviews
@router.get("/")
def get_all_interviews():
    pass

#get interview by id
@router.get("/interview_id")
def get_interview_by_id(interview_id: int):
    pass

#update interview by id
@router.put("/interview_id")
def update_interview_by_id(interview_id: int):
    pass

#delete interview by id
@router.delete("/interview_id")
def delete_interview_by_id(interview_id: int):
    pass


#get interview by time(start_time and end_time)
@router.get("/by-time")
def get_interview_by_time(start_time: str, end_time: str): #We use string because JSON does NOT support datetime or time types
    pass



#@router.get("/interviews")