from pydantic import BaseModel,field
from datetime import datetime

class InterviewCreateRequest(BaseModel):
    candidatename:str=field(min_length=3,max_length=30,example="surname example")
    interviver_name:str
    time:datetime

class InterviewUpdateRequest(BaseModel):
    candidatename:str=field(min_length=3,max_length=30,example="surname example")
    interviver_name:str
    time:datetime    
