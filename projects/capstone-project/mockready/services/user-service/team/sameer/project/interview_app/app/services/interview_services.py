import time

from app.db.db import interviews  

from app.schemas.interview_request import InterviewCreateRequest, InterviewUpdateRequest
from app.exeptions.custom_exception import InterviewNotFoundException
# create interview
def create_interview(request: InterviewCreateRequest):
    new_interview = {
        "id": len(interviews) + 1,            
        "candidate_name": request.candidate_name,
        "interviewer_name": request.interviewer_name,       
        "time": request.time
    }
    interviews.append(new_interview)
    return new_interview


# get all interviews
def get_all_interviews():
    return interviews   


# get interview by id
def get_interview_by_id(interview_id: int):
    for interview in interviews:
        if interview["id"] == interview_id:
            return interview
    raise InterviewNotFoundException(interview_id)                                            



# update interview by id
def update_interview_by_id(interview_id: int, request: InterviewUpdateRequest):
    for interview in interviews:
        if interview["id"] == interview_id:
            interview.update({
                "candidate name": request.candidate_name,
                "interviewer name": request.interviewer_name,
                "time" : request.time
            })
        return interview
    raise InterviewNotFoundException(interview_id)


# delete interview by id
def delete_interview_by_id(interview_id: int):
    for interview in interviews:
        if interview["id"] == interview_id:
            interviews.remove(interview)
        return True
    return False



# get interviews by time (start_time and end_time)
def get_interviews_by_time(start_time: str, end_time: str):
    output_list =[]
    for interview in interviews:
        interview_time = interview["time"]
        if start_time <= interview_time < end_time:
            output_list.append(interview)

        return output_list

