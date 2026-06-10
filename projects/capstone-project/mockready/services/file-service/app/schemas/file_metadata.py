"""
schemas/file_metadata.py

These are NOT database models.
They define what the API accepts and returns.

Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy) ← Phase 2

FileUpdate uses all Optional fields — client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.
"""

from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class FileCreate(BaseModel):
    student_id: UUID
    original_name: str = Field(..., min_length=2, max_length=100)
    stored_path: str = Field(..., min_length=2, max_length=255)
    file_type: str = Field(..., min_length=2, max_length=100)
    size: int = Field(..., gt=0)
    uploaded_at: datetime
    is_active:bool

class FileUpdate(BaseModel):
    original_name: str | None = Field(None, min_length=2, max_length=100)
    stored_path: str | None = Field(None, min_length=2, max_length=255)
    file_type: str | None = Field(None, min_length=2, max_length=100)
    size: int | None = Field(None, gt=0)
    uploaded_at: datetime | None = None


class FileResponse(BaseModel):
    id: UUID
    student_id: UUID
    original_name: str
    stored_path: str
    file_type: str
    size: int
    uploaded_at: datetime
    is_active:bool

    model_config = {
        "from_attributes": True
    }