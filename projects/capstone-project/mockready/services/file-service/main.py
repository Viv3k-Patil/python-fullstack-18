from fastapi import FastAPI,UploadFile,File,Form

app=FastAPI()
resumes={}

@app.get("/health")
def check_health():
    return {
        "msg":"server is running and up"
    }
    
@app.get("upload")    
async def upload(
    name:str,
    email:str,
    file:UploadFile=File(...,example="resume.pdf")
    ):
    
    await content=file.read()
    resumes[file.filename]={
       " name":name,
         "email":email,
         "filename":file.filename,
         "file":file
    }
    return resumes