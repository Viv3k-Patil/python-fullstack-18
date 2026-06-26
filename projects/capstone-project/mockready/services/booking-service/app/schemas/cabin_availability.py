from datetime import datetime
from pydantic import BaseModel


class Cabin_availability(BaseModel):
    start_time: datetime
    end_time: datetime


class Cabin_availability_response(BaseModel):
    cabin_id: int
    campus_id: int
    cabin_number: int


    model_config = {"from_attributes": True}