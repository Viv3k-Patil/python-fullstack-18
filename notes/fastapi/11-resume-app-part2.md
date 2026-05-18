# DAY 2 — Student Execution Script

---

## SETUP

Keep your Day 1 venv active. Install one new package:

```bash
pip install "pydantic[email]"
```

Create this folder structure from scratch:

```
resume-app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── db.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── resume.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── resume.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── exceptions.py
│   │   └── file_utils.py
│   └── routers/
│       ├── __init__.py
│       └── resume_router.py
├── static/
│   └── index.html
└── requirements.txt
```

All `__init__.py` files are empty. Create them all now.

`requirements.txt`:
```
fastapi
uvicorn[standard]
python-multipart
pydantic[email]
```

---

## `app/models/resume.py` — Version 1: Basic model

```python
from pydantic import BaseModel

class ResumeRecord(BaseModel):
    student_name: str
    email: str
    filename: str
```

---

## `app/models/resume.py` — Version 2: Add UUID

```python
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class ResumeRecord(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    student_name: str
    email: str
    filename: str
```

---

## `app/models/resume.py` — FINAL

```python
"""
Domain model / entity for a stored resume.
"""

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ResumeRecord(BaseModel):
    """Represents a resume stored in the in-memory database."""

    id: UUID = Field(default_factory=uuid4)
    student_name: str
    email: str
    original_filename: str
    content_type: str = "application/pdf"
    file_bytes: bytes  # raw PDF bytes held in memory
    uploaded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    file_size_bytes: int

    model_config = {"arbitrary_types_allowed": True}
```

---

## `app/schemas/resume.py` — Version 1: Just upload response

```python
from pydantic import BaseModel
from uuid import UUID

class ResumeUploadResponse(BaseModel):
    id: UUID
    student_name: str
    message: str = "Resume uploaded successfully."
```

---

## `app/schemas/resume.py` — Version 2: Add EmailStr

```python
from pydantic import BaseModel, EmailStr
from uuid import UUID

class ResumeUploadResponse(BaseModel):
    id: UUID
    student_name: str
    email: EmailStr
    message: str = "Resume uploaded successfully."
```

---

## `app/schemas/resume.py` — FINAL

```python
"""
Pydantic schemas for request validation and API response serialization.
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


# ---------------------------------------------------------------------------
# Response schemas
# ---------------------------------------------------------------------------

class ResumeUploadResponse(BaseModel):
    """Returned after a successful upload."""

    id: UUID
    student_name: str
    email: EmailStr
    original_filename: str
    file_size_bytes: int
    uploaded_at: datetime
    message: str = "Resume uploaded successfully."


class ResumeSummary(BaseModel):
    """Lightweight summary used in list responses."""

    id: UUID
    student_name: str
    email: EmailStr
    original_filename: str
    file_size_bytes: int
    uploaded_at: datetime


class ResumeListResponse(BaseModel):
    total: int
    resumes: list[ResumeSummary]


class DeleteResponse(BaseModel):
    message: str
    id: UUID
```

---

## `app/utils/exceptions.py` — Version 1: Base exception only

```python
class ResumeAppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)
```

---

## `app/utils/exceptions.py` — Version 2: Add NotFoundException

```python
class ResumeAppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class ResumeNotFoundException(ResumeAppException):
    def __init__(self, resume_id):
        super().__init__(
            message=f"Resume with id '{resume_id}' not found.",
            status_code=404,
        )
```

---

## `app/utils/exceptions.py` — FINAL

```python
"""
Custom exception hierarchy for the Resume Portal.
"""


class ResumeAppException(Exception):
    """Base exception; caught by the global exception handler."""

    def __init__(self, message: str, status_code: int = 400) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class ResumeNotFoundException(ResumeAppException):
    def __init__(self, resume_id) -> None:
        super().__init__(
            message=f"Resume with id '{resume_id}' not found.",
            status_code=404,
        )


class InvalidFileTypeException(ResumeAppException):
    def __init__(self) -> None:
        super().__init__(
            message="Only PDF files are accepted. Please upload a .pdf file.",
            status_code=415,
        )


class FileTooLargeException(ResumeAppException):
    def __init__(self, max_mb: int) -> None:
        super().__init__(
            message=f"File exceeds the maximum allowed size of {max_mb} MB.",
            status_code=413,
        )


class MissingFieldException(ResumeAppException):
    def __init__(self, field: str) -> None:
        super().__init__(
            message=f"Required field '{field}' is missing or empty.",
            status_code=422,
        )
```

---

## `app/utils/file_utils.py` — Version 1: Content-type check only

```python
from fastapi import UploadFile
from app.utils.exceptions import InvalidFileTypeException

async def validate_pdf_file(file: UploadFile) -> bytes:
    if file.content_type != "application/pdf":
        raise InvalidFileTypeException()

    file_bytes = await file.read()
    return file_bytes
```

---

## `app/utils/file_utils.py` — Version 2: Add extension check

```python
from fastapi import UploadFile
from app.utils.exceptions import InvalidFileTypeException

async def validate_pdf_file(file: UploadFile) -> bytes:
    if file.content_type != "application/pdf":
        raise InvalidFileTypeException()

    filename = file.filename or ""
    if not filename.lower().endswith(".pdf"):
        raise InvalidFileTypeException()

    file_bytes = await file.read()
    return file_bytes
```

---

## `app/utils/file_utils.py` — Version 3: Add magic bytes check

```python
from fastapi import UploadFile
from app.utils.exceptions import InvalidFileTypeException

async def validate_pdf_file(file: UploadFile) -> bytes:
    if file.content_type != "application/pdf":
        raise InvalidFileTypeException()

    filename = file.filename or ""
    if not filename.lower().endswith(".pdf"):
        raise InvalidFileTypeException()

    file_bytes = await file.read()

    if not file_bytes.startswith(b"%PDF-"):
        raise InvalidFileTypeException()

    return file_bytes
```

---

## `app/utils/file_utils.py` — FINAL

```python
"""
Utility helpers for validating uploaded files.
"""

import logging

from fastapi import UploadFile

from app.utils.exceptions import FileTooLargeException, InvalidFileTypeException

logger = logging.getLogger(__name__)

ALLOWED_CONTENT_TYPES = {"application/pdf"}
ALLOWED_EXTENSIONS = {".pdf"}
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024


async def validate_pdf_file(file: UploadFile) -> bytes:
    """
    Reads the file into memory and validates:
    - Content-type header is application/pdf
    - File extension is .pdf
    - File size does not exceed MAX_FILE_SIZE_BYTES
    - File starts with the PDF magic bytes (%PDF-)

    Returns the raw bytes on success; raises appropriate exceptions on failure.
    """
    logger.info(
        "Validating upload | filename=%s | content_type=%s",
        file.filename,
        file.content_type,
    )

    # --- Content-type check ---
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        logger.warning("Rejected upload — bad content-type: %s", file.content_type)
        raise InvalidFileTypeException()

    # --- Extension check ---
    filename = file.filename or ""
    if not any(filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS):
        logger.warning("Rejected upload — bad extension: %s", filename)
        raise InvalidFileTypeException()

    # --- Read into memory ---
    file_bytes: bytes = await file.read()

    # --- Size check ---
    if len(file_bytes) > MAX_FILE_SIZE_BYTES:
        logger.warning(
            "Rejected upload — file too large: %d bytes (max %d MB)",
            len(file_bytes),
            MAX_FILE_SIZE_MB,
        )
        raise FileTooLargeException(MAX_FILE_SIZE_MB)

    # --- Magic bytes check (%PDF-) ---
    if not file_bytes.startswith(b"%PDF-"):
        logger.warning("Rejected upload — file does not start with PDF magic bytes.")
        raise InvalidFileTypeException()

    logger.info("File validation passed | size=%d bytes", len(file_bytes))
    return file_bytes
```

---

## `app/db.py` — Version 1: Bare class

```python
from app.models.resume import ResumeRecord

class InMemoryDatabase:
    def __init__(self):
        self._store = {}

    def insert(self, record: ResumeRecord):
        self._store[record.id] = record
        return record

    def get(self, record_id):
        return self._store.get(record_id)

    def get_all(self):
        return list(self._store.values())

    def delete(self, record_id):
        del self._store[record_id]

db = InMemoryDatabase()
```

---

## `app/db.py` — FINAL

```python
"""
In-memory database for the Resume Portal.
Simulates a database using a plain dict — students replace this with a real DB.
"""

import logging
from typing import Optional
from uuid import UUID

from app.models.resume import ResumeRecord

logger = logging.getLogger(__name__)


class InMemoryDatabase:
    """Thread-unsafe, in-process store (fine for dev / learning purposes)."""

    def __init__(self) -> None:
        self._store: dict[UUID, ResumeRecord] = {}
        logger.info("InMemoryDatabase initialised.")

    # ------------------------------------------------------------------
    # CRUD helpers
    # ------------------------------------------------------------------

    def insert(self, record: ResumeRecord) -> ResumeRecord:
        self._store[record.id] = record
        logger.info("DB insert | id=%s | filename=%s", record.id, record.original_filename)
        return record

    def get(self, record_id: UUID) -> Optional[ResumeRecord]:
        record = self._store.get(record_id)
        if record:
            logger.debug("DB get hit | id=%s", record_id)
        else:
            logger.debug("DB get miss | id=%s", record_id)
        return record

    def get_all(self) -> list[ResumeRecord]:
        records = list(self._store.values())
        logger.debug("DB get_all | count=%d", len(records))
        return records

    def delete(self, record_id: UUID) -> bool:
        if record_id in self._store:
            del self._store[record_id]
            logger.info("DB delete | id=%s", record_id)
            return True
        logger.warning("DB delete miss | id=%s", record_id)
        return False

    def count(self) -> int:
        return len(self._store)


# Singleton instance — import this anywhere in the app
db = InMemoryDatabase()
```

---

## `app/routers/resume_router.py` — Version 1: Upload only, no service yet

```python
from fastapi import APIRouter, File, Form, UploadFile
from app.db import db
from app.models.resume import ResumeRecord
from app.utils.file_utils import validate_pdf_file

router = APIRouter()

@router.post("/upload")
async def upload_resume(
    student_name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = File(...),
):
    file_bytes = await validate_pdf_file(file)
    record = ResumeRecord(
        student_name=student_name,
        email=email,
        original_filename=file.filename,
        file_bytes=file_bytes,
        file_size_bytes=len(file_bytes),
    )
    db.insert(record)
    return {"id": str(record.id), "message": "uploaded"}
```

---

## `app/routers/resume_router.py` — Version 2: Add response_model

```python
from fastapi import APIRouter, File, Form, UploadFile, status
from app.db import db
from app.models.resume import ResumeRecord
from app.schemas.resume import ResumeUploadResponse
from app.utils.file_utils import validate_pdf_file

router = APIRouter()

@router.post("/upload", response_model=ResumeUploadResponse, status_code=201)
async def upload_resume(
    student_name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = File(...),
):
    file_bytes = await validate_pdf_file(file)
    record = ResumeRecord(
        student_name=student_name,
        email=email,
        original_filename=file.filename,
        file_bytes=file_bytes,
        file_size_bytes=len(file_bytes),
    )
    db.insert(record)
    return ResumeUploadResponse(
        id=record.id,
        student_name=record.student_name,
        email=record.email,
        original_filename=record.original_filename,
        file_size_bytes=record.file_size_bytes,
        uploaded_at=record.uploaded_at,
    )
```

---

## `app/routers/resume_router.py` — FINAL (Day 2 version, service wiring comes Day 3)

```python
"""
Resume API Router.
All endpoints are prefixed with /api/resumes (configured in main.py).
"""

import logging
from uuid import UUID

from fastapi import APIRouter, File, Form, UploadFile, status
from fastapi.responses import Response

from app.db import db
from app.models.resume import ResumeRecord
from app.schemas.resume import (
    DeleteResponse,
    ResumeListResponse,
    ResumeSummary,
    ResumeUploadResponse,
)
from app.utils.exceptions import ResumeNotFoundException
from app.utils.file_utils import validate_pdf_file

logger = logging.getLogger(__name__)

router = APIRouter()


# ---------------------------------------------------------------------------
# POST /api/resumes/upload
# ---------------------------------------------------------------------------
@router.post(
    "/upload",
    response_model=ResumeUploadResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Upload a student resume (PDF only)",
)
async def upload_resume(
    student_name: str = Form(..., description="Full name of the student"),
    email: str = Form(..., description="Student email address"),
    file: UploadFile = File(..., description="PDF resume file (max 5 MB)"),
) -> ResumeUploadResponse:
    """
    Upload a resume for a student.

    - **student_name**: Full name of the student
    - **email**: Valid student email
    - **file**: A PDF document (≤ 5 MB)
    """
    logger.info("POST /upload | student=%s | email=%s", student_name, email)
    file_bytes = await validate_pdf_file(file)
    record = ResumeRecord(
        student_name=student_name.strip(),
        email=email.strip().lower(),
        original_filename=file.filename or "resume.pdf",
        file_bytes=file_bytes,
        file_size_bytes=len(file_bytes),
    )
    db.insert(record)
    return ResumeUploadResponse(
        id=record.id,
        student_name=record.student_name,
        email=record.email,
        original_filename=record.original_filename,
        file_size_bytes=record.file_size_bytes,
        uploaded_at=record.uploaded_at,
    )


# ---------------------------------------------------------------------------
# GET /api/resumes/
# ---------------------------------------------------------------------------
@router.get(
    "/",
    response_model=ResumeListResponse,
    summary="List all uploaded resumes",
)
def list_resumes() -> ResumeListResponse:
    """Returns metadata for every resume currently in the store."""
    logger.info("GET / — listing all resumes")
    records = db.get_all()
    summaries = [
        ResumeSummary(
            id=r.id,
            student_name=r.student_name,
            email=r.email,
            original_filename=r.original_filename,
            file_size_bytes=r.file_size_bytes,
            uploaded_at=r.uploaded_at,
        )
        for r in records
    ]
    return ResumeListResponse(total=len(summaries), resumes=summaries)


# ---------------------------------------------------------------------------
# GET /api/resumes/{resume_id}/download
# ---------------------------------------------------------------------------
@router.get(
    "/{resume_id}/download",
    summary="Download a resume PDF by ID",
    response_class=Response,
    responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "PDF file download",
        },
        404: {"description": "Resume not found"},
    },
)
def download_resume(resume_id: UUID) -> Response:
    """
    Stream the PDF bytes for the requested resume.
    The response includes Content-Disposition: attachment so browsers
    trigger a file-download dialog.
    """
    logger.info("GET /%s/download", resume_id)
    record = db.get(resume_id)
    if not record:
        raise ResumeNotFoundException(resume_id)
    return Response(
        content=record.file_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="{record.original_filename}"',
            "Content-Length": str(record.file_size_bytes),
        },
    )


# ---------------------------------------------------------------------------
# DELETE /api/resumes/{resume_id}
# ---------------------------------------------------------------------------
@router.delete(
    "/{resume_id}",
    response_model=DeleteResponse,
    summary="Delete a resume by ID",
    status_code=status.HTTP_200_OK,
)
def delete_resume(resume_id: UUID) -> DeleteResponse:
    """Permanently removes the resume from the in-memory store."""
    logger.info("DELETE /%s", resume_id)
    if not db.get(resume_id):
        raise ResumeNotFoundException(resume_id)
    db.delete(resume_id)
    return DeleteResponse(message="Resume deleted successfully.", id=resume_id)
```

---

## `app/main.py` — DAY 2 FINAL

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from app.routers import resume_router
from app.utils.exceptions import ResumeAppException

app = FastAPI(title="Resume Portal API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.exception_handler(ResumeAppException)
async def handle_app_exception(request: Request, exc: ResumeAppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )


@app.exception_handler(Exception)
async def handle_unknown(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal server error."})


app.include_router(resume_router.router, prefix="/api/resumes", tags=["Resumes"])


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
def frontend():
    return FileResponse("static/index.html")
```

```bash
uvicorn app.main:app --reload
```

Visit: http://localhost:8000
Swagger: http://localhost:8000/docs
