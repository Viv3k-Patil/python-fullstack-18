from app.schemas.interview_request import InterviewUpdateRequest

#Create  POST interview
def create_interview():   
  pass
    
#Create GET interview

def show_interviews():
  pass

#Create GET interview by id
def get_interviews_by_id(id:int):
   pass

#Create PUT / UPDTE interview{id=int , name=str}
def update_interview(id:int,request:InterviewUpdateRequest):
    pass

# DELET interview by id

def delete_interviwe_by_id(interview_id:int):
    pass

#get DATE AND TIME interviewm{time=IST,Date=int}

def get_time(start_time:str,end_time:str):
    pass