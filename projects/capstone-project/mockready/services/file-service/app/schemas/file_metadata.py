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

from datetime import date


class FileCreate(BaseModel):
    student_id: int
    student_name: str = Field(..., min_length=2, max_length=100)
    
class FileUpdate(BaseModel):
    student_id: int = Field(..., gt=0)
    student_name: str | None = Field(None, min_length=2, max_length=100)
    stored_path: str | None = Field(None, min_length=2, max_length=255)
    file_type: str | None = Field(None, min_length=2, max_length=100)
    size_bytes: int | None = Field(None, gt=0)
    uploaded_at: date | None = None


class FileResponse(BaseModel):
    id: int
    student_id: int
    student_name: str
    stored_path: str
    file_type: str
    size_bytes: int
    uploaded_at: date |None=None
    is_active:bool


    model_config = {
        "from_attributes": True
    }