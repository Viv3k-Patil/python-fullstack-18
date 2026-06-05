
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

from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


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
    schedule_at: datetime | None = None
    decline_count: int | None = None


class BookingResponse(BaseModel):
    booking_id: int
    student_id: int
    trainer_id: int
    cabin_id: int
    campus_id: int
    interview_type: str
    status: str
    schedule_at: datetime | None
    decline_count: int
    created_at: datetime

class Config:
    from_attributes = True