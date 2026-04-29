"""
Resume API Router.
All endpoints are prefixed with /api/resumes (configured in main.py).
"""

import logging
from uuid import UUID

from fastapi import APIRouter, File, Form, UploadFile, status
from fastapi.responses import Response

from app.schemas.resume import DeleteResponse, ResumeListResponse, ResumeUploadResponse
from app.services.resume_services import resume_service

logger = logging.getLogger(__name__)

router = APIRouter()


# ---------------------------------------------------------------------------
# POST /api/resumes/upload
# ---------------------------------------------------------------------------
@router.post(
    "/resumes",
    response_model=ResumeUploadResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Upload a student resume (PDF only)",
)
async def upload_resume(
    student_name: str = Form(..., description="Full name of the student"),
    email: str = Form(..., description="Student email address"),
    file: UploadFile = File(..., description="PDF resume file (max 5 MB)"),
) -> ResumeUploadResponse:
    """
    Upload a resume for a student.

    - **student_name**: Full name of the student
    - **email**: Valid student email
    - **file**: A PDF document (≤ 5 MB)
    """
    logger.info("POST /upload | student=%s | email=%s", student_name, email)
    return await resume_service.upload_resume(student_name, email, file)


# ---------------------------------------------------------------------------
# GET /api/resumes/
# ---------------------------------------------------------------------------
@router.get(
    "/resumes",
    response_model=ResumeListResponse,
    summary="List all uploaded resumes",
)
def list_resumes() -> ResumeListResponse:
    """Returns metadata for every resume currently in the store."""
    logger.info("GET / — listing all resumes")
    return resume_service.list_resumes()


# ---------------------------------------------------------------------------
# GET /api/resumes/{resume_id}/
# ---------------------------------------------------------------------------
@router.get(
    "resumes/{resume_id}",
    summary="Download a resume PDF by ID",
    response_class=Response,
    responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "PDF file download",
        },
        404: {"description": "Resume not found"},
    },
)
def download_resume(resume_id: UUID) -> Response:
    """
    Stream the PDF bytes for the requested resume.
    The response includes Content-Disposition: attachment so browsers
    trigger a file-download dialog.
    """
    logger.info("GET /%s/download", resume_id)
    record = resume_service.get_resume_bytes(resume_id)
    return Response(
        content=record.file_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="{record.original_filename}"',
            "Content-Length": str(record.file_size_bytes),
        },
    )


# ---------------------------------------------------------------------------
# DELETE /api/resumes/{resume_id}
# ---------------------------------------------------------------------------
@router.delete(
    "resumes/{resume_id}",
    response_model=DeleteResponse,
    summary="Delete a resume by ID",
    status_code=status.HTTP_200_OK,
)
def delete_resume(resume_id: UUID) -> DeleteResponse:
    """Permanently removes the resume from the in-memory store."""
    logger.info("DELETE /%s", resume_id)
    return resume_service.delete_resume(resume_id)