
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
    student_id: UUID
    trainer_id: UUID
    cabin_id: UUID
    campus_id: UUID
    interview_type: str
    status: str


class BookingUpdate(BaseModel):
    trainer_id: UUID | None = None
    cabin_id: UUID | None = None
    interview_type: str | None = None
    status: str | None = None
    schedule_at: datetime | None = None
    decline_count: int | None = None


class BookingResponse(BaseModel):
    id: UUID
    student_id: UUID
    trainer_id: UUID
    cabin_id: UUID
    campus_id: UUID
    interview_type: str
    status: str
    schedule_at: datetime | None
    decline_count: int
    created_at: datetime

    class Config:
        from_attributes = True