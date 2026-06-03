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
from datetime import date
from typing import Optional

class BatchCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    course:str = Field(..., min_length=2, max_length=100)
    campus_id: int 


class BatchUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    course:str | None = Field(None, min_length=2, max_length=100)
    campus_id:int
    is_active: bool | None = None   
     

class BatchResponse(BaseModel):
    batch_id: int
    campus_id: int
    name: str
    course:str
    start_date:Optional[date]=None
    end_time:Optional[date]=None
    is_active: bool

    model_config = {"from_attributes": True}  # ready for ORM in Phase 2    