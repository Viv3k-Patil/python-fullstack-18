from fastapi import UploadFile
from app.utils.file_utils import validate_pdf_file
from app.schemas.resumes import ResumeUploadResponse,ResumeListResponse,ResumeSummary,DeleteResponse
from app.models.resume import ResumeRecord
from app.db.resumes_db import db
from app.exceptions.custom_exceptions import ResumeNotFoundException
from uuid import UUID
import logging

logger=logging.getLogger(__name__)

class ResumeServices():
    def __init__(self):
        print("service class has been initilized")
    
    async def upload_resume(
        self,
        student_name:str,
        email:str,
        file:UploadFile              
    )->ResumeUploadResponse:
        
        file_bytes= await validate_pdf_file(file)
        
        #upload in db
        record=ResumeRecord(
            student_name=student_name,
            email=email,
            original_filename=file.filename,
            file_bytes=file_bytes,
            file_size_bytes= len(file_bytes)
        )
        
        db.insert(record)
        logger.info("file uploaded succesfully")

        return ResumeUploadResponse(
            id=record.id,
            student_name=record.student_name,
            email=record.email,
            original_filename=record.original_filename,
            file_size_bytes=record.file_size_bytes,
            uploaded_at=record.uploaded_at  
        )
    
    def list_resumes(self)->ResumeListResponse:
        
        records=db.get_all()
        record_schema=[]
        for record in records:
            each_resume_summary=ResumeSummary(
                id=record.id,
                student_name=record.student_name,
                email=record.email,
                original_filename=record.original_filename,
                file_size_bytes=record.file_size_bytes,
                uploaded_at=record.uploaded_at
            )
            record_schema.append(each_resume_summary)
         
 
        return ResumeListResponse(
            total=len(records),
            resumes=record_schema
        )
        
    def get_resume_bytes(self,resume_id:UUID)->ResumeRecord:
        logger.info("")
        record_model=db.get(resume_id)
        return record_model
    
    def delete_resume(self,resume_id:UUID)->DeleteResponse:
        if not db.delete(resume_id):
            raise ResumeNotFoundException(resume_id)
        return DeleteResponse(
            id=resume_id,
            message="resume deleted succesfuully"
        )
            
        

resume_service=ResumeServices()
