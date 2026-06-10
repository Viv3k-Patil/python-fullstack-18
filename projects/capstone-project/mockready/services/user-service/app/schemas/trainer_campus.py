"""
schemas/trainer_campus.py

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
from datetime import datetime

class TrainerCampusCreate(BaseModel):
    trainer_id: int = Field(..., ge=1)
    campus_id: int = Field(..., ge=1, le=50)
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)  


class TrainerCampusUpdate(BaseModel):    
    trainer_id: int | None = Field(None, ge=1)
    campus_id: int | None = Field(None, ge=1, le=50)
    is_active: bool | None = None   
    created_at: datetime | None = None  # Optional, but usually not updated 


    
class TrainerCampusResponse(BaseModel):
    trainer_campus_id: int
    campus_id: int
    trainer_id: int
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}  # ready for ORM in Phase 2

