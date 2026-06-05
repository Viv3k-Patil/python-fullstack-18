<<<<<<< HEAD
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
=======
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date, datetime

class BatchBase(BaseModel):
    name: str = Field(..., description="Name of the batch, e.g., Python_FullStack_18")
    course: str = Field(..., description="Name of the course")
    start_date: date
    end_date: date

class BatchCreate(BatchBase):
    campus_id: UUID = Field(..., description="The campus this batch belongs to")

class BatchUpdate(BaseModel):
    name: str | None = None
    course: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    campus_id: UUID | None = None

class BatchResponse(BatchBase):
    id: UUID
>>>>>>> 93280eaa (Batch Created)
    campus_id: UUID
    is_active: bool
    created_at: datetime

<<<<<<< HEAD
    model_config = {"from_attributes": True}  # ready for ORM in Phase 2    
=======
    class Config:
        from_attributes = True
>>>>>>> 93280eaa (Batch Created)
