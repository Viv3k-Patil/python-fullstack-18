from pydantic import BaseModel, Field
from datetime import datetime

class InterviewCreateRequest(BaseModel):
    candidate_name: str = Field(min_length=2, max_length=100, example="name surname")
    interviewer_name: str
    time: datetime


class InterviewUpdateRequest(BaseModel):
    candidate_name: str = Field(min_length=2, max_length=100, example="name surname")
    interviewer_name: str
    time: datetime
<<<<<<< HEAD
=======

>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
