"""
schemas/trainer_availability.py

These are NOT database models.
They define what the API accepts and returns.

Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy) ← Phase 2

trainer_availability_Update uses all Optional fields — client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.
"""

from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime,time,date
from typing import Optional

class Trainer_AvailabilityCreate(BaseModel):
        tainer_id : UUID = Field(...)
        campus_id : UUID = Field(...)
        date : date
        start_time : time
        end_time : time
        is_booked : bool

class Trainer_AvailabilityUpdate(BaseModel):
        trainer_id: UUID | None = Field(None)
        campus_id: UUID| None = Field(None)
        date: Optional[date] = None
        start_time: Optional[date] = None
        end_time: Optional[date] = None
        is_active: bool | None = None


class Trainer_AvailabilityResponse(BaseModel):
        id : UUID
        tainer_id : UUID
        campus_id : UUID
        date : date
        start_time : time
        end_time : time
        is_booked : bool


<<<<<<< HEAD

        model_config = {"from_attributes": True}

=======
        model_config = {"from_attributes": True}



>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
