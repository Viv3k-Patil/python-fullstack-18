"""
Pydantic schemas for request validation and api response.
"""
from pydantic import BaseModel
from uuid import UUID , uuid4   
from datetime import datetime
#---------------------------------------
# Response Schemas
#---------------------------------------
class ResumeUploadResponse(BaseModel):
    """Return after succesfull upload of a resume"""
    
    id:UUID
    student_name:str
    email:str
    orignal_filename:str
    msg:str="Resume uploaded succesfully"
    file_size_bytes:int
    uploaded_at:datetime
    
class ResumeSummary(BaseModel):
    """Lightweight summary for resumelist"""    
    id:UUID
    student_name:str
    email:str
    orignal_filename:str
    file_size_bytes:int
    uploded_at:datetime
    
class ResumeListResponse(BaseModel):
    total:int
    resume:list[ResumeSummary]   
    
class ResumeDeleteResponse(BaseModel):
    id:UUID
    msg:str="Resume deleted succesfully"    
    
class ResumeUploadRequest(BaseModel):
    student_name:str
    email:str
    uploadresume:str="application/pdf"      