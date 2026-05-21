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