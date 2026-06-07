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
from datetime import datetime, time

class TrainerAvailabilityCreate(BaseModel):
    trainer_id: int = Field(..., ge=1)
    campus_id: int = Field(..., ge=1)
    start_time: datetime = Field(...)
    end_time: datetime = Field(...)     
    date: datetime = Field(...)
   # created_at: datetime = Field(default_factory=datetime.utcnow)


class TrainerAvailabilityUpdate(BaseModel):
    trainer_id: int | None = Field(None, ge=1)
    campus_id: int | None = Field(None, ge=1)
    start_time: datetime | None = Field(None)
    end_time: datetime | None = Field(None)     
    date: datetime | None = Field(None)
   # is_active: bool | None = None

class TrainerAvailabilityResponse(BaseModel):
        trainer_availability_id: int
        trainer_id: int
        campus_id: int
        start_time: time
        end_time: time
        date: datetime
        is_active: bool
        created_at: datetime
        
        model_config = {"from_attributes": True}