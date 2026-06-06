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
from uuid import UUID, uuid4
from datetime import datetime


class TrainerCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    city: str = Field(..., min_length=2, max_length=100)
    address: str = Field(..., min_length=5, max_length=255)
    experience_years: int = 1
    skills: list[str] = Field(default_factory=list)
    specialization: str | None = None
    rating: float | None = Field(None, ge=1, le=5)


class TrainerUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    city: str | None = Field(None, min_length=2, max_length=100)
    address: str | None = Field(None, min_length=5, max_length=255)
    experience_years: int | None = Field(None, ge=1, le=50)
    skills: list[str] = Field(default_factory=list)
    specialization: str | None = None
    rating: float | None = Field(None, ge=1, le=5)
    is_active: bool | None = None


class TrainerResponse(BaseModel):
    id: UUID
    name: str
    city: str
    address: str
    experience_years: int = 1
    skills: list[str]
    specialization: str | None
    rating: float | None
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}  # ready for ORM in Phase 2