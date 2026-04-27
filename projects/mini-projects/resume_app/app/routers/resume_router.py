"""
Resume portal API
"""

from fastapi import APIRouter, Form, UploadFile, File
from app.schemas.resume import ResumeUploadResponse, ResumeListResponse
from app.services import resume_services

router = APIRouter()


# POST /resumes Upload resume endpoint
@router.post(
        "/resumes",
        response_model=ResumeUploadResponse,
        status_code=201,
        summary="Upload a resume"
    )
async def upload_resume(
        student_name: str = Form(..., description="Name of the student uploading the resume"),
        email: str = Form(..., description="Email of the student uploading the resume"),
        uploaded_resume: UploadFile = File(..., description="The resume file to upload (PDF format)")
    )-> ResumeUploadResponse:
    """
    Upload resume for a student in pdf format
    """
    return await resume_service.upload_resume(student_name, email, uploaded_resume)


# GET /resumes get list of all resumes
@router.get(
        "/resumes",
        response_model=ResumeListResponse,
        summary="List all the uploaded resumes"
    )
def list_resumes():
    """Return list of all the resumes and its metadata except resume"""
    return resume_service.list_resumes()

# GET /resumes/{resume_id}
@router.get(
        "/resumes/{resume_id}",
        response_model=Response,
        summary="downloads a resume"
    )
def download_resume(resume_id: str):
    resume = resume_service.download_resume(resume_id)
    return Response(
        content=resume["file"],
        media_type="application/pdf",
        headers = {"Content-Disposition": f"attachment; filename={resume['filename']}"}
    )

# delete resume
@router.delete("/resumes/{resume_id}")
def delete_resume(resume_id: str):
    # CRDUI
    del resumes[resume_id]
    return {
        "msg": "deleted"
    }