<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
from fastapi import FastAPI
from fastapi.responses import  FileResponse
from app.routers.resume_router import router as resume_router
from fastapi.staticfiles import StaticFiles
from app.exceptions.global_exception_handler import global_exception_handler
app = FastAPI()

# --------------------------------------------------------
# Register global exception handler
# --------------------------------------------------------
global_exception_handler(app)

app.include_router(resume_router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
def show_frontend():
    return FileResponse("static/index.html")

<<<<<<< HEAD
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
"""
Resume Upload/Download Application
Entry point for the FastAPI application.
"""

import logging
import sys
from contextlib import asynccontextmanager
<<<<<<< HEAD
<<<<<<< HEAD

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles


from app.router import resume_router as router
=======
=======
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
from fastapi.middleware.cors import CORSMiddleware


from app.middleware.logging_middleware import LoggingMiddleware
from app.routers import resume_router
<<<<<<< HEAD
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
from app.exceptions.global_exception_handler import global_exception_handler

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
<<<<<<< HEAD
<<<<<<< HEAD
#app.add_middleware(LoggingMiddleware)
=======
app.add_middleware(LoggingMiddleware)
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
app.add_middleware(LoggingMiddleware)
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06

# ---------------------------------------------------------------------------
# Static files (frontend)
# ---------------------------------------------------------------------------
<<<<<<< HEAD
<<<<<<< HEAD
#app.mount("/static", StaticFiles(directory="static"), name="static")
=======
app.mount("/static", StaticFiles(directory="static"), name="static")
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
app.mount("/static", StaticFiles(directory="static"), name="static")
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06

# ---------------------------------------------------------------------------
# Global exception handler
# ---------------------------------------------------------------------------
global_exception_handler(app)


# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------
<<<<<<< HEAD
<<<<<<< HEAD
app.include_router(router.router, prefix="/api/resumes", tags=["Resumes"])
=======
app.include_router(resume_router.router, prefix="/api/resumes", tags=["Resumes"])
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
app.include_router(resume_router.router, prefix="/api/resumes", tags=["Resumes"])
>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06


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
<<<<<<< HEAD
<<<<<<< HEAD
    return FileResponse("static/index.html")
=======
    return FileResponse("static/index.html")

>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
=======
    return FileResponse("static/index.html")

>>>>>>> 4aacc19637dc0ce44fffc32356a97238fbedee06
