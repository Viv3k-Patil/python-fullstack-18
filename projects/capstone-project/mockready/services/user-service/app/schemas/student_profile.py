"""
schemas/student_profile.py

These are NOT database models.
They define what the API accepts and returns.

Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy) ← Phase 2

student_profile_Update uses all Optional fields — client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.
"""

from pydantic import BaseModel, Field
from datetime import datetime

class StudentProfileCreate(BaseModel):
    user_id: int = Field(...)
    batch_id: int = Field(...)
    skills: str= Field(..., min_length=5, max_length=255)
    enrollment_number: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class StudentProfileUpdate(BaseModel):
    user_id: int | None = Field(None, ge=1)
    batch_id: int | None = Field(None, ge=1)
    skills: str | None = Field(None, min_length=5, max_length=255)
    enrollment_number: str | None = Field(None)
    is_active: bool | None = None

class StudentProfileResponse(BaseModel):
    student_id: int
    user_id: int
    batch_id: int
    skills: str
    enrollment_number: str
    is_active: bool
    created_at: datetime
    

    model_config = {"from_attributes": True}

