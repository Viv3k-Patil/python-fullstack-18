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
    campus_id: UUID
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True