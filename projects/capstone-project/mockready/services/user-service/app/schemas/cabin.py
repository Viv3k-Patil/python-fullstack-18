
"""
schemas/cabin.py
These are NOT database models.
They define what the API accepts and returns.
Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy) ← Phase 2
CabinUpdate uses all Optional fields — client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.
"""
from pydantic import BaseModel,Field
class CabinCreate(BaseModel):
    campus_id:int = Field(...,ge=1,le=50)
    cabin_number:int = Field(...,ge=1,le=50)
    
    
class CabinUpdate(BaseModel):    
    cabin_number:int | None=None
    is_active:bool | None=None
    
class CabinResponse(BaseModel):
    cabin_id:int
    campus_id:int
    is_active:bool        
    cabin_number:int


    model_config = {"from_attributes": True} 

