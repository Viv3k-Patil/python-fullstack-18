<<<<<<< HEAD
import logging
from app.db.resume_db import db
from app.schemas.resume import ResumeUploadResponse, ResumeListResponse, DeleteResponse
from app.models.resume import ResumeRecord
from app.utils.file_utils import validate_pdf_file
from fastapi import UploadFile
from uuid import UUID


logger = logging.getLogger(__name__)

class ResumeService:
    def __init__(self):
        print("service class has been initialized")

    def upload_resume(
            self,
            student_name: str,
            email: str,
            file: UploadFile
    ) -> ResumeUploadResponse:
        # check if file is correct
        logger.info(
            "validating upload | filename= "
        )
        file_bytes = validate_pdf_file(file)

        # upload in db
        record = ResumeRecord(
            student_name=student_name,
            email=email,
            original_file_name=file.filename,
            file_bytes= file_bytes,
            file_size_bytes=len(file_bytes)
        )

        db.insert(record)
        logger.info("file uploaded successfully")

        return ResumeUploadResponse(
            id= record.id,
=======
"""
Service layer — all business logic lives here.
Routers call services; services call the DB and utilities.
"""

import logging
from uuid import UUID

from fastapi import UploadFile

from app.db.db import db
from app.models.resume import ResumeRecord
from app.schemas.resume import (
    DeleteResponse,
    ResumeListResponse,
    ResumeSummary,
    ResumeUploadRequest,
    ResumeUploadResponse,
)
from app.exceptions.custom_exception import ResumeNotFoundException
from app.utils.file_utils import validate_pdf_file

logger = logging.getLogger(__name__)


class ResumeService:
    """Encapsulates all resume-related operations."""

    # ------------------------------------------------------------------
    # Upload
    # ------------------------------------------------------------------
    async def upload_resume(
        self,
        student_name: str,
        email: str,
        file: UploadFile,
    ) -> ResumeUploadResponse:
        logger.info(
            "upload_resume called | student=%s | email=%s | filename=%s",
            student_name,
            email,
            file.filename,
        )

        # Validate form fields through request schema
        request_data = ResumeUploadRequest(student_name=student_name, email=email)

        # File validation — returns raw bytes if valid
        file_bytes = await validate_pdf_file(file)

        # Persist to in-memory DB
        record = ResumeRecord(
            student_name=request_data.student_name,
            email=request_data.email,
            original_filename=file.filename or "resume.pdf",
            file_bytes=file_bytes,
            file_size_bytes=len(file_bytes),
        )
        db.insert(record)

        logger.info(
            "Resume stored | id=%s | student=%s | size=%d bytes",
            record.id,
            record.student_name,
            record.file_size_bytes,
        )

        return ResumeUploadResponse(
            id=record.id,
<<<<<<< HEAD
>>>>>>> 8ee2b4665817a3550d1895555cb83836724637f7
=======
>>>>>>> ea3141f4e13ba1afa5fb4513ad9ddaf7245c89d2
>>>>>>> 1cbf00331909a46a54aae8247e9731cb55397e45
            student_name=record.student_name,
            email=record.email,
            original_filename=record.original_filename,
            file_size_bytes=record.file_size_bytes,
<<<<<<< HEAD
            uploaded_at=record.uploaded_at
        )
    
    def list_resumes(self) -> ResumeListResponse:
        records = db.get_all()
        records_schema = []
        for record in records:
            each_resume_summary = ResumeSummary(
                id= record.id,
                student_name=record.student_name,
                email=record.email,
                original_filename=record.original_filename,
                file_size_bytes=record.file_size_bytes,
                uploaded_at=record.uploaded_at
            )
            records_schema.append(each_resume_summary)

        return ResumeListResponse(
            total=len(records),
            resumes=records_schema
        )
    
    def get_resume_bytes(self, resume_id: UUID) -> ResumeRecord:
        logger.info("")
        record_model = db.get(resume_id)
        return record_model

    def delete_resume(resume_id: UUID) -> DeleteResponse:
        if not db.delete(resume_id):
            raise ResumeNotFoundException(resume_id)

        return DeleteResponse(
            message="resume deleted successfully",
            id=resume_id
        )

=======
            uploaded_at=record.uploaded_at,
        )

    # ------------------------------------------------------------------
    # List
    # ------------------------------------------------------------------
    def list_resumes(self) -> ResumeListResponse:
        logger.info("list_resumes called | total=%d", db.count())
        records = db.get_all()
        summaries = [
            ResumeSummary(
                id=r.id,
                student_name=r.student_name,
                email=r.email,
                original_filename=r.original_filename,
                file_size_bytes=r.file_size_bytes,
                uploaded_at=r.uploaded_at,
            )
            for r in records
        ]
        return ResumeListResponse(total=len(summaries), resumes=summaries)

    # ------------------------------------------------------------------
    # Download (returns raw bytes + metadata)
    # ------------------------------------------------------------------
    def get_resume_bytes(self, resume_id: UUID) -> ResumeRecord:
        logger.info("get_resume_bytes called | id=%s", resume_id)
        record = db.get(resume_id)
        if not record:
            raise ResumeNotFoundException(resume_id)
        logger.info(
            "Serving download | id=%s | filename=%s | size=%d bytes",
            record.id,
            record.original_filename,
            record.file_size_bytes,
        )
        return record

    # ------------------------------------------------------------------
    # Delete
    # ------------------------------------------------------------------
    def delete_resume(self, resume_id: UUID) -> DeleteResponse:
        logger.info("delete_resume called | id=%s", resume_id)
        if not db.get(resume_id):
            raise ResumeNotFoundException(resume_id)
        db.delete(resume_id)
        return DeleteResponse(message="Resume deleted successfully.", id=resume_id)


# Singleton
<<<<<<< HEAD
>>>>>>> 8ee2b4665817a3550d1895555cb83836724637f7
=======
>>>>>>> ea3141f4e13ba1afa5fb4513ad9ddaf7245c89d2
>>>>>>> 1cbf00331909a46a54aae8247e9731cb55397e45
resume_service = ResumeService()