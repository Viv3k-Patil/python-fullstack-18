"""
Domain model / entity for a stored resume.
"""

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ResumeRecord(BaseModel):
    """Represents a resume stored in the in-memory database."""

    id: UUID = Field(default_factory=uuid4)
    student_name: str
    email: str
    original_filename: str
    content_type: str = "application/pdf"
    file_bytes: bytes  # raw PDF bytes held in memory
    uploaded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    file_size_bytes: int

    model_config = {"arbitrary_types_allowed": True}