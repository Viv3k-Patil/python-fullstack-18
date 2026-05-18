"""
Pydantic schemas for request validation and API response serialization.
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


# ---------------------------------------------------------------------------
<<<<<<< HEAD
=======
# Request schemas
# ---------------------------------------------------------------------------

class ResumeUploadRequest(BaseModel):
    """Validates the text fields from the upload form."""

    student_name: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    email: EmailStr


# ---------------------------------------------------------------------------
>>>>>>> 8ee2b4665817a3550d1895555cb83836724637f7
# Response schemas
# ---------------------------------------------------------------------------

class ResumeUploadResponse(BaseModel):
    """Returned after a successful upload."""

    id: UUID
    student_name: str
    email: EmailStr
    original_filename: str
    file_size_bytes: int
    uploaded_at: datetime
    message: str = "Resume uploaded successfully."

<<<<<<< HEAD
=======

>>>>>>> 8ee2b4665817a3550d1895555cb83836724637f7
class ResumeSummary(BaseModel):
    """Lightweight summary used in list responses."""

    id: UUID
    student_name: str
    email: EmailStr
    original_filename: str
    file_size_bytes: int
    uploaded_at: datetime


class ResumeListResponse(BaseModel):
    total: int
    resumes: list[ResumeSummary]


class DeleteResponse(BaseModel):
    message: str
    id: UUID