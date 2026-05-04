"""
Resume Router API
"""
from fastapi import APIRouter,Form,UploadFile , Response,File
from app.schemas.resumes import ResumeUploadResponse,ResumeListResponse
from app.services import resume_services
resumes={}

router=APIRouter()

#post/resume/upload resume
@router.post("/resumes",
            response_model=ResumeUploadResponse,
            status_code=200,
            summary="Upload a resume"
            )
async def upload_resume(
        student_name:str=Form(...,description="name of the student uploading resume"),
        email:str=Form(...,description="email of the student uploading resume"),
        upload_resume:UploadFile=File(...,description="resume file uploade(file formate)")
    )->ResumeUploadResponse:
    
    return await resume_services.upload_resume(student_name,email,upload_resume)

""""
   upload resume for a student in pdf  format
"""

#Get List of all resumes

@router.get("/resumes",
            response_model=ResumeListResponse,
            summary="list of all resumes")
def list_resume():
    """Return list of all resumes and its meta data except resume"""
    return resume_services.list_resumes()

#GET/resumes/resume_id     
@router.get("/resumes{resume_id}",
            response_model=Response,
            summary="download resume"
            )
def download_resume(resume_id:str): 
       resume=resume_services.download_resume(resume_id)
       return Response(
           content=resume["file"],
           media_type="application/pdf",
           headers={"Content-Disposition": f"attachment; filename={resume['filename']}"}
       )
  
@router.delete("/resumes{resume_id}") 
def delete_resume(resume_id:str):
    del resumes[resume_id]
    return {
        "msg":f"delete the resume {resume_id}"
    }
    
@router.put("/resumes{resume_id}")  
def update_resume(
    resume_id:str,
    student_name:str=Form(...),
    email:str=Form(...),
    upload_resume:UploadFile=None          
):
   
     # Check if resume exists
     if resume_id in resumes:
     
       resume_data= resumes[resume_id].update({
        "student_name":student_name,
        "email":email,
        "filename":upload_resume.filename if upload_resume else None
    })
    
       return {
                "resume_id":resume_id,
                "resume_data":resume_data  ,
                "msg":"Resume Updated succesfully"
            }