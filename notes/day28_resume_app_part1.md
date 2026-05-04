# DAY 1 — Student Execution Script

---

## SETUP

```bash
mkdir resume-app
cd resume-app
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-multipart
```

Create folder structure:
```
resume-app/
├── main.py
└── static/
    └── index.html   ← given to you, place it here
```

---

## `main.py` — Version 1: Hello FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume Portal is running"}
```

```bash
uvicorn main:app --reload
```

---

## `main.py` — Version 2: Add URL parameter

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume Portal is running"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello {name}"}
```

---

## `main.py` — Version 3: Add in-memory storage

```python
from fastapi import FastAPI

app = FastAPI()

resumes = {}

@app.get("/")
def home():
    return {"message": "Resume Portal is running", "total": len(resumes)}
```

---

## `main.py` — Version 4: Bare file upload

```python
from fastapi import FastAPI, UploadFile

app = FastAPI()

resumes = {}

@app.post("/upload")
async def upload_resume(file: UploadFile):
    contents = await file.read()
    resumes[file.filename] = contents
    return {"message": "uploaded", "filename": file.filename}
```

---

## `main.py` — Version 5: Add student name and email

```python
from fastapi import FastAPI, UploadFile, Form

app = FastAPI()

resumes = {}

@app.post("/upload")
async def upload_resume(
    student_name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = None,
):
    contents = await file.read()
    resumes[email] = {
        "student_name": student_name,
        "email": email,
        "filename": file.filename,
        "file": contents,
    }
    return {"message": "uploaded", "student_name": student_name}
```

---

## `main.py` — Version 6: Add list endpoint

```python
from fastapi import FastAPI, UploadFile, Form

app = FastAPI()

resumes = {}

@app.post("/upload")
async def upload_resume(
    student_name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = None,
):
    contents = await file.read()
    resumes[email] = {
        "student_name": student_name,
        "email": email,
        "filename": file.filename,
        "file": contents,
    }
    return {"message": "uploaded", "student_name": student_name}


@app.get("/resumes")
def list_resumes():
    result = []
    for key, r in resumes.items():
        result.append({
            "id": key,
            "student_name": r["student_name"],
            "email": r["email"],
            "filename": r["filename"],
        })
    return {"total": len(result), "resumes": result}
```

---

## `main.py` — Version 7: Add download endpoint

```python
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import Response

app = FastAPI()

resumes = {}

@app.post("/upload")
async def upload_resume(
    student_name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = None,
):
    contents = await file.read()
    resumes[email] = {
        "student_name": student_name,
        "email": email,
        "filename": file.filename,
        "file": contents,
    }
    return {"message": "uploaded", "student_name": student_name}


@app.get("/resumes")
def list_resumes():
    result = []
    for key, r in resumes.items():
        result.append({
            "id": key,
            "student_name": r["student_name"],
            "email": r["email"],
            "filename": r["filename"],
        })
    return {"total": len(result), "resumes": result}


@app.get("/resumes/{resume_id}/download")
def download_resume(resume_id: str):
    resume = resumes.get(resume_id)
    return Response(
        content=resume["file"],
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={resume['filename']}"},
    )
```

---

## `main.py` — Version 8: Add delete endpoint

```python
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import Response

app = FastAPI()

resumes = {}

@app.post("/upload")
async def upload_resume(
    student_name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = None,
):
    contents = await file.read()
    resumes[email] = {
        "student_name": student_name,
        "email": email,
        "filename": file.filename,
        "file": contents,
    }
    return {"message": "uploaded", "student_name": student_name}


@app.get("/resumes")
def list_resumes():
    result = []
    for key, r in resumes.items():
        result.append({
            "id": key,
            "student_name": r["student_name"],
            "email": r["email"],
            "filename": r["filename"],
        })
    return {"total": len(result), "resumes": result}


@app.get("/resumes/{resume_id}/download")
def download_resume(resume_id: str):
    resume = resumes.get(resume_id)
    return Response(
        content=resume["file"],
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={resume['filename']}"},
    )


@app.delete("/resumes/{resume_id}")
def delete_resume(resume_id: str):
    del resumes[resume_id]
    return {"message": "deleted"}
```

---

## `main.py` — Version 9: Connect the frontend (FINAL DAY 1)

```python
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import Response, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

resumes = {}

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
def frontend():
    return FileResponse("static/index.html")


@app.post("/upload")
async def upload_resume(
    student_name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = None,
):
    contents = await file.read()
    resumes[email] = {
        "student_name": student_name,
        "email": email,
        "filename": file.filename,
        "file": contents,
    }
    return {"message": "uploaded", "student_name": student_name}


@app.get("/resumes")
def list_resumes():
    result = []
    for key, r in resumes.items():
        result.append({
            "id": key,
            "student_name": r["student_name"],
            "email": r["email"],
            "filename": r["filename"],
        })
    return {"total": len(result), "resumes": result}


@app.get("/resumes/{resume_id}/download")
def download_resume(resume_id: str):
    resume = resumes.get(resume_id)
    return Response(
        content=resume["file"],
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={resume['filename']}"},
    )


@app.delete("/resumes/{resume_id}")
def delete_resume(resume_id: str):
    del resumes[resume_id]
    return {"message": "deleted"}
```

```bash
uvicorn main:app --reload
```

Visit: http://localhost:8000
Swagger: http://localhost:8000/docs

---

## THINGS TO TRY AND BREAK BEFORE DAY 2

1. Upload a `.jpg` file — does it accept it?
2. Upload two resumes with the same email — what happens to the first?
3. Download using an ID that doesn't exist — what error do you get?
4. Leave `student_name` empty — does it still upload?
