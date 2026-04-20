from fastapi import HTTPException   
from pydantic import BaseModel
from datetime import datetime   
from typing import List


class InterviewResponse(BaseModel):
    id: int
    candidate_name: str
    interviewer_name: str
    time: datetime
    duration_minutes: int   

class InterviewResponseList(BaseModel):
    Interview : List[InterviewResponse]
