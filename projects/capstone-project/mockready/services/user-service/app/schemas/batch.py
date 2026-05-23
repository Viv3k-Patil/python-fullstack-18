"""
schemas/batch.py

These are NOT database models.
They define what the API accepts and returns.

Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy) ← Phase 2

BatchUpdate uses all Optional fields — client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.
"""
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class BatchCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    campus_id: UUID 


class BatchUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    campus_id: UUID | None = None
    is_active: bool | None = None   
     

class BatchResponse(BaseModel):
    id: UUID
    name: str
    campus_id: UUID
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}  # ready for ORM in Phase 2