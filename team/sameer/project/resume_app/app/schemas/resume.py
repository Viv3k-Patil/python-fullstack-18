"""
Pydantic schemas for request validation and API response serialization.
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


# ---------------------------------------------------------------------------
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