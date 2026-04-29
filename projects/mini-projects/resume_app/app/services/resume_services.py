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
            student_name=record.student_name,
            email=record.email,
            original_filename=record.original_filename,
            file_size_bytes=record.file_size_bytes,
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

resume_service = ResumeService()