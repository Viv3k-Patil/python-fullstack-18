from app.schemas.interview_request import InterviewCreateRequest, InterviewUpdateRequest
# create interview
def create_interview(request: InterviewCreateRequest):
    pass    


# get all interviews
def get_all_interviews():
    pass


# get interview by id
def get_interview_by_id(interview_id: int):
    pass                                        



# update interview by id
def update_interview_by_id(interview_id: int, request: InterviewUpdateRequest):
    pass


# delete interview by id
def delete_interview_by_id(interview_id: int):
    pass


# get interviews by time (start_time and end_time)
def get_interviews_by_time(start_time: str, end_time: str):
    pass


