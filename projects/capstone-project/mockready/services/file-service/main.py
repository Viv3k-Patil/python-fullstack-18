from fastapi import FastAPI,UploadFile,File
from app.routes.health import router as health_router

app=FastAPI()

app.include_router(health_router)

@app.get("/health")
def check_health():
    return {
        "msg":"server is running and up"
    }
    
# @app.get("upload")    
# async def upload(
#     name:str,
#     email:str,
#     file:UploadFile=File(...,example="resume.pdf")
#     ):
    
#     await content=file.read()
#     resumes[file.filename]={
#        " name":name,
#          "email":email,
#          "filename":file.filename,
#          "file":file
#     }
#     return resumes