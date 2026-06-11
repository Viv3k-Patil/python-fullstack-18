"""
schemas/users.py

These are NOT database models.
They define what the API accepts and returns.

Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy) ← Phase 2

UserUpdate uses all Optional fields — client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.
"""
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
    role: str = Field(..., min_length=2, max_length=20)
    campus_id: int
    created_at: datetime = Field(default_factory=datetime.now)


class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=50)
    email: EmailStr | None = None
    hashed_password: str | None = Field(None, min_length=6, max_length=250)
    role: str | None = Field(None, min_length=2, max_length=20)
    campus_id: int | None = None
    is_active: bool | None = None


class UserResponse(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    role: str
    campus_id: int | None
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}