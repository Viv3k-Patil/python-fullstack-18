
from pydantic import BaseModel, Field
from datetime import datetime


class InterviewCreateRequest(BaseModel):
    candidate_name : str = Field(min_length=2, max_length = 100) #json_schema_extra={"example": "mounika"}
    interview_name  : str
    time : datetime

class InterviewUpdateRequest(BaseModel):
    candidate_name : str = Field(min_length=2, max_length = 100)#json_schema_extra={"example": "mounika"})
    interview_name  : str
    time : datetime
