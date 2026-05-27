"""
schemas/trainer_campus.py

These are NOT database models.
They define what the API accepts and returns.

Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy) ← Phase 2

TrainerUpdate uses all Optional fields — client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.
"""

import uuid

from pydantic import BaseModel, Field
from uuid import UUID, uuid4    
from datetime import datetime

class TrainerCampusCreate(BaseModel):
    campus_id: UUID
    trainer_id: UUID
    location: str = Field(..., min_length=2, max_length=100)
    capacity: int = Field(..., ge=1)    


class TrainerCampusUpdate(BaseModel):
    campus_id: UUID | None = None
    trainer_id: UUID | None = None
    location: str | None = Field(None, min_length=2, max_length=100)
    capacity: int | None = Field(None, ge=1)    
    is_active: bool | None = None   

    
class TrainerCampusResponse(BaseModel):
    id: UUID
    campus_id: UUID
    trainer_id: UUID
    location: str
    capacity: int
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}  # ready for ORM in Phase 2

