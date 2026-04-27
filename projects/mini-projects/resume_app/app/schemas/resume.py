"""
Pyndatic schemas for request validtion and api response serialization.
"""

from datetime import datetime
from pydantic import BaseModel
from uuid import UUID, uuid4


# --------------------------------------------------------------------------
# Response schemas
# --------------------------------------------------------------------------
class ResumeUploadResponse(BaseModel):
    """Returned after a successful upload of a resume."""

    id: UUID
    student_name: str
    email: str
    original_filename: str
    message: str = "resume uploaded successfully"
    file_size_bytes: int
    uploaded_at: datetime

class ResumeSummary(BaseModel):
    """Lightweight summary used in list resposnes."""

    id: UUID
    student_name: str
    email: str
    original_filename: str
    file_size_bytes: int
    uploaded_at: datetime

class ResumeListResponse(BaseModel):
    total: int
    resume: list[ResumeSummary]

class ResumeDeleteResponse(BaseModel):
    id: UUID
    message: str


# Create ResumeUploadRequest schema