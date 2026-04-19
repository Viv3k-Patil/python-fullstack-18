from pydantic import BaseModel,Field
from datetime import datetime
from typing import List

class InterviewResponse(BaseModel):
    id:int
    candidate_name:str
    Interviver_name:str
    time:datetime

class InterviewResponseList(BaseModel):
    Interviews=List[InterviewResponse]
  
    