# DAY 3 — Student Execution Script

---

## SETUP

No new packages needed. Add two new folders:

```
resume-app/
├── app/
│   ├── __init__.py
│   ├── main.py               ← rewrite today
│   ├── db.py                 ← done
│   ├── models/
│   │   └── resume.py         ← done
│   ├── schemas/
│   │   └── resume.py         ← adding ResumeUploadRequest today
│   ├── services/             ← NEW
│   │   ├── __init__.py
│   │   └── resume_service.py ← NEW
│   ├── middleware/           ← NEW
│   │   ├── __init__.py
│   │   └── logging_middleware.py ← NEW
│   ├── utils/
│   │   ├── exceptions.py     ← done
│   │   └── file_utils.py     ← done
│   └── routers/
│       └── resume_router.py  ← update today
├── static/
│   └── index.html
├── requirements.txt
└── run.py                    ← NEW
```

Create `app/services/` and `app/middleware/` with empty `__init__.py` files.

---

## `app/schemas/resume.py` — Add ResumeUploadRequest (FINAL)

Add `ResumeUploadRequest` at the top of the existing schemas file:

```python
"""
Pydantic schemas for request validation and API response serialization.
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


# ---------------------------------------------------------------------------
# Request schemas
# ---------------------------------------------------------------------------

class ResumeUploadRequest(BaseModel):
    """Validates the text fields from the upload form."""

    student_name: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    email: EmailStr


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

## `app/services/resume_service.py` — Version 1: Upload only, bare

```python
from fastapi import UploadFile
from app.db import db
from app.models.resume import ResumeRecord
from app.schemas.resume import ResumeUploadRequest, ResumeUploadResponse
from app.utils.file_utils import validate_pdf_file

class ResumeService:

    async def upload_resume(self, student_name: str, email: str, file: UploadFile):
        request_data = ResumeUploadRequest(student_name=student_name, email=email)
        file_bytes = await validate_pdf_file(file)
        record = ResumeRecord(
            student_name=request_data.student_name,
            email=request_data.email,
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

resume_service = ResumeService()
```

---

## `app/services/resume_service.py` — Version 2: Add list and delete

```python
from uuid import UUID
from fastapi import UploadFile
from app.db import db
from app.models.resume import ResumeRecord
from app.schemas.resume import (
    ResumeUploadRequest, ResumeUploadResponse,
    ResumeSummary, ResumeListResponse, DeleteResponse,
)
from app.utils.exceptions import ResumeNotFoundException
from app.utils.file_utils import validate_pdf_file

class ResumeService:

    async def upload_resume(self, student_name: str, email: str, file: UploadFile):
        request_data = ResumeUploadRequest(student_name=student_name, email=email)
        file_bytes = await validate_pdf_file(file)
        record = ResumeRecord(
            student_name=request_data.student_name,
            email=request_data.email,
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

    def list_resumes(self) -> ResumeListResponse:
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

    def get_resume_bytes(self, resume_id: UUID) -> ResumeRecord:
        record = db.get(resume_id)
        if not record:
            raise ResumeNotFoundException(resume_id)
        return record

    def delete_resume(self, resume_id: UUID) -> DeleteResponse:
        if not db.get(resume_id):
            raise ResumeNotFoundException(resume_id)
        db.delete(resume_id)
        return DeleteResponse(message="Resume deleted successfully.", id=resume_id)

resume_service = ResumeService()
```

---

## `app/services/resume_service.py` — FINAL

```python
"""
Service layer — all business logic lives here.
Routers call services; services call the DB and utilities.
"""

import logging
from uuid import UUID

from fastapi import UploadFile

from app.db import db
from app.models.resume import ResumeRecord
from app.schemas.resume import (
    DeleteResponse,
    ResumeListResponse,
    ResumeSummary,
    ResumeUploadRequest,
    ResumeUploadResponse,
)
from app.utils.exceptions import ResumeNotFoundException
from app.utils.file_utils import validate_pdf_file

logger = logging.getLogger(__name__)


class ResumeService:
    """Encapsulates all resume-related operations."""

    # ------------------------------------------------------------------
    # Upload
    # ------------------------------------------------------------------
    async def upload_resume(
        self,
        student_name: str,
        email: str,
        file: UploadFile,
    ) -> ResumeUploadResponse:
        logger.info(
            "upload_resume called | student=%s | email=%s | filename=%s",
            student_name,
            email,
            file.filename,
        )

        # Validate form fields through request schema
        request_data = ResumeUploadRequest(student_name=student_name, email=email)

        # File validation — returns raw bytes if valid
        file_bytes = await validate_pdf_file(file)

        # Persist to in-memory DB
        record = ResumeRecord(
            student_name=request_data.student_name,
            email=request_data.email,
            original_filename=file.filename or "resume.pdf",
            file_bytes=file_bytes,
            file_size_bytes=len(file_bytes),
        )
        db.insert(record)

        logger.info(
            "Resume stored | id=%s | student=%s | size=%d bytes",
            record.id,
            record.student_name,
            record.file_size_bytes,
        )

        return ResumeUploadResponse(
            id=record.id,
            student_name=record.student_name,
            email=record.email,
            original_filename=record.original_filename,
            file_size_bytes=record.file_size_bytes,
            uploaded_at=record.uploaded_at,
        )

    # ------------------------------------------------------------------
    # List
    # ------------------------------------------------------------------
    def list_resumes(self) -> ResumeListResponse:
        logger.info("list_resumes called | total=%d", db.count())
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

    # ------------------------------------------------------------------
    # Download (returns raw bytes + metadata)
    # ------------------------------------------------------------------
    def get_resume_bytes(self, resume_id: UUID) -> ResumeRecord:
        logger.info("get_resume_bytes called | id=%s", resume_id)
        record = db.get(resume_id)
        if not record:
            raise ResumeNotFoundException(resume_id)
        logger.info(
            "Serving download | id=%s | filename=%s | size=%d bytes",
            record.id,
            record.original_filename,
            record.file_size_bytes,
        )
        return record

    # ------------------------------------------------------------------
    # Delete
    # ------------------------------------------------------------------
    def delete_resume(self, resume_id: UUID) -> DeleteResponse:
        logger.info("delete_resume called | id=%s", resume_id)
        if not db.get(resume_id):
            raise ResumeNotFoundException(resume_id)
        db.delete(resume_id)
        return DeleteResponse(message="Resume deleted successfully.", id=resume_id)


# Singleton
resume_service = ResumeService()
```

---

## `app/routers/resume_router.py` — FINAL (slim — calls service only)

```python
"""
Resume API Router.
All endpoints are prefixed with /api/resumes (configured in main.py).
"""

import logging
from uuid import UUID

from fastapi import APIRouter, File, Form, UploadFile, status
from fastapi.responses import Response

from app.schemas.resume import DeleteResponse, ResumeListResponse, ResumeUploadResponse
from app.services.resume_service import resume_service

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
    return await resume_service.upload_resume(student_name, email, file)


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
    return resume_service.list_resumes()


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
    record = resume_service.get_resume_bytes(resume_id)
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
    return resume_service.delete_resume(resume_id)
```

---

## `app/middleware/logging_middleware.py` — Version 1: print version

```python
import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"{request.method} {request.url.path} → {response.status_code} | {elapsed_ms:.1f}ms")
        return response
```

---

## `app/middleware/logging_middleware.py` — FINAL

```python
"""
Middleware that logs every incoming request and outgoing response.
"""

import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        start = time.perf_counter()
        logger.info(
            "→ REQUEST  | %s %s | client=%s",
            request.method,
            request.url.path,
            request.client.host if request.client else "unknown",
        )

        try:
            response: Response = await call_next(request)
        except Exception:
            logger.exception("Middleware caught unhandled exception.")
            raise

        elapsed_ms = (time.perf_counter() - start) * 1000
        logger.info(
            "← RESPONSE | %s %s | status=%d | %.1f ms",
            request.method,
            request.url.path,
            response.status_code,
            elapsed_ms,
        )
        return response
```

---

## `app/main.py` — Version 1: Add logging config only

```python
import logging
import sys
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from app.routers import resume_router
from app.utils.exceptions import ResumeAppException

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Resume Portal API", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.exception_handler(ResumeAppException)
async def handle_app_exception(request: Request, exc: ResumeAppException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

@app.exception_handler(Exception)
async def handle_unknown(request: Request, exc: Exception):
    logger.exception("Unhandled exception on path=%s", request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Internal server error."})

app.include_router(resume_router.router, prefix="/api/resumes", tags=["Resumes"])

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/", include_in_schema=False)
def frontend():
    return FileResponse("static/index.html")
```

---

## `app/main.py` — Version 2: Add lifespan

```python
import logging
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from app.routers import resume_router
from app.utils.exceptions import ResumeAppException

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Resume API starting up...")
    yield
    logger.info("🛑 Resume API shutting down...")


app = FastAPI(title="Resume Portal API", version="1.0.0", lifespan=lifespan)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.exception_handler(ResumeAppException)
async def handle_app_exception(request: Request, exc: ResumeAppException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

@app.exception_handler(Exception)
async def handle_unknown(request: Request, exc: Exception):
    logger.exception("Unhandled exception on path=%s", request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Internal server error."})

app.include_router(resume_router.router, prefix="/api/resumes", tags=["Resumes"])

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/", include_in_schema=False)
def frontend():
    return FileResponse("static/index.html")
```

---

## `app/main.py` — FINAL

```python
"""
Resume Upload/Download Application
Entry point for the FastAPI application.
"""

import logging
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.middleware.logging_middleware import LoggingMiddleware
from app.routers import resume_router
from app.utils.exceptions import ResumeAppException

# ---------------------------------------------------------------------------
# Logging configuration
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Lifespan (startup / shutdown)
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Resume API starting up...")
    yield
    logger.info("🛑 Resume API shutting down...")


# ---------------------------------------------------------------------------
# App factory
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Resume Portal API",
    description="Industry-grade API for uploading and downloading student resumes (PDF only).",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# ---------------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggingMiddleware)

# ---------------------------------------------------------------------------
# Static files (frontend)
# ---------------------------------------------------------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# ---------------------------------------------------------------------------
# Global exception handler
# ---------------------------------------------------------------------------
@app.exception_handler(ResumeAppException)
async def resume_app_exception_handler(request: Request, exc: ResumeAppException):
    logger.warning("Application exception: %s | path=%s", exc.message, request.url.path)
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception on path=%s", request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Internal server error."})


# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------
app.include_router(resume_router.router, prefix="/api/resumes", tags=["Resumes"])


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------
@app.get("/api/health", tags=["Health"])
async def health_check():
    logger.debug("Health check called.")
    return {"status": "ok", "service": "Resume Portal API"}


# ---------------------------------------------------------------------------
# Root → serve index.html
# ---------------------------------------------------------------------------
from fastapi.responses import FileResponse  # noqa: E402


@app.get("/", include_in_schema=False)
async def serve_frontend():
    return FileResponse("static/index.html")
```

---

## `run.py` — FINAL

```python
"""
Run the Resume Portal with:
    python run.py
or:
    uvicorn app.main:app --reload
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
```

```bash
python run.py
```

Visit: http://localhost:8000
Swagger: http://localhost:8000/api/docs
ReDoc: http://localhost:8000/api/redoc
