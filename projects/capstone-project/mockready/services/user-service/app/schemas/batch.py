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
from datetime import date, datetime


class BatchCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    campus_id: int = Field(...,ge=1,le=50)
    course : str =Field(..., min_length=2, max_length=100)
    start_date : date = Field(default_factory=date)
    end_date : date = Field(default_factory=date)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class BatchUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    campus_id: int | None = None
    is_active: bool | None = None  
    course  : str |    None = None 
    start_date : date | None = None
    end_date : date | None = None
    created_at: datetime | None = None
     

class BatchResponse(BaseModel):
    batch_id: int
    name: str
    course:str
    campus_id: int
    start_date: date | None = None
    end_date: date | None = None
    is_active: bool
    created_at: datetime | None = None

    model_config = {"from_attributes": True}  # ready for ORM in Phase 2    