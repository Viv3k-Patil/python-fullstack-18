"""
schemas/cabin.py

These are NOT database models.
They define what the API accepts and returns.

Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy) ← Phase 2


These are NOT database models.
They define what the API accepts and returns.
Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy) ← Phase 2
CabinUpdate uses all Optional fields — client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.
"""

from pydantic import BaseModel
from uuid import UUID
        
class CreateCabin(BaseModel):
    campus_id:UUID
    cabin_number:int
    is_active:bool
    
class UpdateCabin(BaseModel):    
    cabin_number:int | None=None
    is_active:bool | None=None
    
class CabinResponse(BaseModel):
    id:UUID
    campus_id:UUID
    cabin_number:int=1
    is_active:bool        