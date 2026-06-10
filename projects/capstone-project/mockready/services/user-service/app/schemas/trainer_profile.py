"""
schemas/trainer_profile.py

These are NOT database models.
They define what the API accepts and returns.

Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy) ← Phase 2

TrainerUpdate uses all Optional fields — client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.
"""

from pydantic import BaseModel, Field
from datetime import datetime


class TrainerProfileCreate(BaseModel):
    user_id: int = Field(..., ge=1)
    experience_years: int = 1
    skills: str = Field(..., max_length=200)
    rating: float | None = Field(None, ge=1, le=5)
    total_sessions: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)

class TrainerProfileUpdate(BaseModel):
    user_id: int | None = Field(None, ge=1)
    experience_years: int | None = Field(None, ge=1, le=50)
    skills: str | None = Field(None, max_length=200)
    rating: float | None = Field(None, ge=1, le=5)
    total_sessions: int | None = Field(None, ge=0)  
    is_active: bool | None = None


class TrainerProfileResponse(BaseModel):
    trainer_id: int
    user_id: int
    experience_years: int = 1
    skills: str
    rating: float | None
    is_active: bool
    total_sessions: int
    created_at: datetime

    model_config = {"from_attributes": True}  # ready for ORM in Phase 2