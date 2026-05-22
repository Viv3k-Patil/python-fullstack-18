from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field

class StudentProfileCreate(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., min_length=5, max_length=100)
    phone: str = Field(..., min_length=10, max_length=15)
    enrollment_number: str = Field(..., min_length=5, max_length=20)
    skills: str = Field(..., min_length=2, max_length=255)
    
class StudentProfileUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[str] = Field(None, min_length=5, max_length=100)
    phone: Optional[str] = Field(None, min_length=10, max_length=15)
    enrollment_number: Optional[str] = Field(None, min_length=5, max_length=20)
    skills: Optional[str] = Field(None, min_length=2, max_length=255)
    is_active: Optional[bool] = None


class StudentProfileResponse(BaseModel):
    id: UUID
    full_name: str
    email: str
    phone: str
    enrollment_number: str
    skills: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}
