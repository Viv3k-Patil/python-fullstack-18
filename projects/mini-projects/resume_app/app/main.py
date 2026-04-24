from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import Response, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# -----------------------------------------------------------
# Fake databse
# -----------------------------------------------------------
resumes = {}

# @app.get("/")
# def root():
#     return {
#         "message":"Resume portal is running"
#     }

@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "message": f"Hello, {name}"
    }

@app.post("/resumes")
async def upload_resume(
        student_name: str = Form(...),
        email: str = Form(...),
        uploaded_resume: UploadFile = None
    ):
    contents = await uploaded_resume.read()

    # save to fake database CRUDI
    resumes[uploaded_resume.filename] = {
        "student_name": student_name,
        "email": email,
        "filename": uploaded_resume.filename,
        "file": contents
    }
    print(resumes)

    return {
        "message": "upload successful",
        "filename": f"file uploaded: {uploaded_resume.filename}"
    }


# see all resumes
@app.get("/resumes")
def list_resumes():
    result = []
    # email, studentname, filename, id
    for key, resume in resumes.items():
        result.append({
            "id": key,
            "student_name": resume["student_name"],
            "email": resume["email"],
            "filename": resume["filename"]
        })
    return {
        "total": len(result),
        "resumes": result
    }

# download resume
@app.get("/resumes/{resume_id}")
def download_resume(resume_id: str):
    resume = resumes.get(resume_id)
    return Response(
        content=resume["file"],
        media_type="application/pdf",
        headers = {"Content-Disposition": f"attachment; filename={resume['filename']}"}
    )

# delete resume
@app.delete("/resumes/{resume_id}")
def delete_resume(resume_id: str):
    # CRDUI
    del resumes[resume_id]
    return {
        "msg": "deleted"
    }


# # update resume
# @app.put("/resumes/{resume_id}")
# def udpate_resume(resume_id: str, )


# {
#     'resume.pdf': {
#                     'student_name': 'Vivek Patil',
#                     'email': 'vivek.patil@gmail.com',
#                     'filename': 'resume.pdf',
#                     'file': b''
#                 }
 
# }
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
def show_frontend():
    return FileResponse("static/index.html")
