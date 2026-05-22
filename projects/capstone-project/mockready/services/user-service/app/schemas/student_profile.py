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
from uuid import UUID, uuid4    
from datetime import datetime
from typing import Optional


class StudentProfileCreate(BaseModel):
    user_id: UUID = Field(...)
    batch_id: UUID = Field(...)
    skills: list[str] = Field(default_factory=list)
    enrollment_number: str = Field(...)
    name: str = Field(...)
    city: str = Field(...)
    address: str = Field(...)
    interests: list[str] = Field(default_factory=list)

class StudentProfileUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    interests: Optional[list[str]] = None
    skills: Optional[list[str]] = None
    is_active: Optional[bool] = None

class StudentProfileResponse(BaseModel):
    id: UUID
    user_id: UUID
    batch_id: UUID
    enrollment_number: str  
    name: str
    city: str
    address: str
    interests: list[str]
    skills: list[str]   
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}

