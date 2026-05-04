"""DOMAIN MODEL / INTITY TO STORE resume in database"""

from pydantic import BaseModel,Field
from uuid import UUID , uuid4
from datetime import datetime
class ResumeRecord(BaseModel):
    """Represents a resume records in  memory-database"""
    id:UUID= Field(default_factory=uuid4)
    student_name:str
    email:str
    orignal_filename:str
    filename:str    
    conten_type:str="Application/pdf"
    file_bytes:bytes
    uploaded_at:datetime =Field(default_factory=lambda:datetime.now())
    file_size_byte:int
    
    
    model_config={"arbitrary_types_allowed":True} #bytes sathi use kela jata to read bytes 
    