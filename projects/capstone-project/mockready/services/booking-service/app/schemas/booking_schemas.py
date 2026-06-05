
"""
schemas/booking.py

This file contains:
1. Request schemas
2. Response schemas
3. Validation layer

Pydantic handles:
- Request validation
- Response serialization
- Type checking
"""
<<<<<<< HEAD


from datetime import datetime
from pydantic import BaseModel


=======
from datetime import datetime
from pydantic import BaseModel

>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
class BookingCreate(BaseModel):
    student_id: int
    trainer_id: int
    cabin_id: int
    campus_id: int
    interview_type: str
    status: str


class BookingUpdate(BaseModel):
    trainer_id: int | None = None
    cabin_id: int | None = None
    interview_type: str | None = None
    status: str | None = None
<<<<<<< HEAD
    schedule_at: datetime | None = None
=======
    scheduled_at: datetime | None = None
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
    decline_count: int | None = None


class BookingResponse(BaseModel):
    booking_id: int
    student_id: int
    trainer_id: int
    cabin_id: int
    campus_id: int
    interview_type: str
    status: str
<<<<<<< HEAD
    schedule_at: datetime | None
    decline_count: int
    created_at: datetime

    class Config:
        from_attributes = True
=======
    scheduled_at: datetime | None
    decline_count: int
    created_at: datetime

   
    model_config = {"from_attributes": True}
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
