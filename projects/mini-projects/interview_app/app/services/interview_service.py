import datetime
from app.schemas.interview_request import InterviewUpdateRequest, InterviewCreateRequest
from app.db.db import interviews
from app.exceptions.custom_exceptions import InterviewNotFoundException

# create interview service method
def create_interview(request: InterviewCreateRequest):
    new_interview = {
        "id": len(interviews) + 1,
        "candidate_name": request.candidate_name,
        "interviewer_name": request.interviewer_name,
        "time": request.time
    }
    interviews.append(new_interview)
    return new_interview
    

# get all interview service method
def get_all_interviews():
    return interviews

# get interview by id
def get_interview_by_id(interview_id: int):
    for each_interview in interviews:
        if each_interview["id"] == interview_id:
            return each_interview
    raise InterviewNotFoundException(interview_id)


# udpate interview by id
def update_interview_by_id(interview_id: int, request: InterviewUpdateRequest):
    for each_interview in interviews:
        if each_interview["id"] == interview_id:
            each_interview.update({
                "candidate_name": request.candidate_name,
                "interviewer_name" : request.interviewer_name,
                "time": request.time
            })
            return each_interview
    raise InterviewNotFoundException(interview_id)

# delete interview service method
def delete_interview(interview_id: int):
    for each_interview in interviews:
        if each_interview["id"] == interview_id:
            interviews.remove(each_interview)
            return True
    return False

# get interview by time
def get_interview_by_time(start_time: datetime.datetime, end_time: datetime.datetime):
    output_list = []
    for each_interview in interviews:
        interview_actual_time = each_interview["time"]
        if start_time <= interview_actual_time < end_time:
            output_list.append(each_interview)
    return output_list
