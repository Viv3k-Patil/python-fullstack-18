
"""""
schema/batch.py

These is not a database models.
They define what the API accepts and returns

Rule:
    schemas/  ->what the API sees (Patdyntic)
    models/  ->what the db sees (SQLAlschemy) <- phase 2
    
BatchUpdate uses all optional fields -client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.    
"""""

from pydantic import BaseModel,Field
from uuid import UUID,uuid4
from datetime import datetime


class BatchCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    campus_id: UUID
    course: str = Field(..., min_length=2, max_length=50)
    start_date: datetime
    end_date: datetime
    is_active: bool
    
class UpdateBatch(BaseModel):
    name:str|None = Field(None,min_length=2,max_length=50)
    course:str|None=Field(None,min_length=2,max_length=50)
    start_date:datetime|None=Field(None)
    end_date:datetime|None=Field(None) 
    
class BatchResponse(BaseModel):
    id:UUID
    campus_id: UUID 
    name:str
    course:str
    start_date:datetime
    end_date:datetime
    is_active:bool=True
    
    
model_config = {"from_attributes": True}    

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
from email.policy import default

from pydantic import BaseModel, Field
from datetime import date, datetime

class BatchCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    campus_id: int = Field(...,ge=1,le=50)
    course : str =Field(..., min_length=2, max_length=100)
    start_date : date = Field(default_factory=date)
    end_date : date = Field(default_factory=date)
   # created_at: datetime = Field(default_factory=datetime.utcnow)


class BatchUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    campus_id: int | None = None
    is_active: bool | None = None  
    course  : str |    None = None 
     

class BatchResponse(BaseModel):
    batch_id: int
    name: str
    course:str
    campus_id: int
    start_date:date
    end_date:date
    is_active: bool
    #created_at: datetime

    model_config = {"from_attributes": True}  # ready for ORM in Phase 2    

