"""
pyndantic schemas for request validation and api response serialization

"""

from pydantic import BaseModel
from  uuid import UUID, uuid4
from datetime import datetime
#----------------------------------------
# Response Schemas
#----------------------------------------

class ResumeUploadResponse(BaseModel):
    """Returned after a successful upload of a resume."""

    id : UUID
    student_name : str
    email : str
    original_filename : str
    message : str = "Resume uploaded successfully..!"
    file_size_bytes : int
    uploaded_at :datetime

class ResumeSummary(BaseModel):
    """Lightwight summary used in list summary"""
    id : UUID
    student_name : str
    email : str
    orignal_filename : str
    file_size_bytes : int
    uploaded_at : datetime


class ResumeListResponse(BaseModel):
    total : int
    resume : list[ResumeSummary]


class ResumeDeleteResponse(BaseModel):
   id : UUID
   message : str
