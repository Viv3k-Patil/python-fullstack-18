from pydantic import BaseModel,field
from datetime import datetime

class interviewCreateRequest(BaseModel):
       candidate_name : str = field(min_length = 3 , max_length = 30 , example = "name surname")
       interviewer_name : str
       time : datetime

class interviewUpdateRequest(BaseModel):
       candidate_name : str = field(min_length = 3 , max_length = 30 , example = "name surname")
       interviwer_name : str
       time : datetime