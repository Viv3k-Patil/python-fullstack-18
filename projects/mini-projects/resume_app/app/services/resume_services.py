from app.db.resumes_db import resumes
from fastapi.responses import Response
from app.schemas.resumes import ResumeUploadResponse 
from fastapi import UploadFile
async def upload_resume(student_name,email,upload_resume):    
    contents= await upload_resume.read()  
    
    resumes[upload_resume.filename] ={
        "student_name":student_name,
        "email":email,
        "filename":upload_resume.filename,
        "file":contents
    }
    print(resumes)
        
    return {
            "message":"resume upload sucessfully",
            "filename":f"file name is {upload_resume.filename}"
        }
    
def list_resumes():
     result=[]
     #studentname,emil,filename,resume_id
     for key,resume in resumes.items():
         result.append({
             "resume_id":key,
             "student_name":resume["student_name"],
             "email":resume["email"],
             "filename":resume["filename"]
         })
         
     return {
         "total":len(result),
         "resumes":result
     }        
     
def download_resume(resume_id:str):
        resumes.get(resume_id)
        return Response(
           content=resumes["file"],
           media_type="application/pdf",
           headers={"Content-Disposition": f"attachment; filename={resumes['filename']}"}
       )
        
def delete_resume(resume_id:str):
    del resumes[resume_id]
    return {
        "msg":f"delete the resume {resume_id}"
    }        
        
     