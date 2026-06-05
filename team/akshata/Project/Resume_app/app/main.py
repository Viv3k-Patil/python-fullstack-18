
from fastapi import FastAPI , uploafile

app = FastAPI()

resumes = {}

@app.get("/")
def root():
    return {
        "message": "Resume portal is running"
    }

@app.get("/hello/{name}")
def say_hello(name : str):
    return{
        "message": "f Hello {name}"
    }


@app.post("/upload")
def upload_resume(uploaded_resume : uploafile ):
   content = uploaded_resume.read()
   resumes[uploaded_resume.filename] = content
   
    return
        {
       "message": "File succssfully uploaded..!"
       "file_name" : f"file uploaded: {uploaded_resume.filename}"
    }