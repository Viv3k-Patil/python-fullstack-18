from app.db.resume_db import resumes 


def upload_resume(student_name, email, uploaded_resume):
    contents = await uploaded_resume.read()

    # save to fake database CRUDI
    resumes[uploaded_resume.filename] = {
        "student_name": student_name,
        "email": email,
        "filename": uploaded_resume.filename,
        "file": contents,
    }
    print(resumes)

    return {
        "message": "upload successful",
        "filename": f"file uploaded: {uploaded_resume.filename}"
    }


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

def download_resume(resume_id):
    return {}
