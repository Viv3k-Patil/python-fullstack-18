<<<<<<< HEAD
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import Response, FileResponse
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
=======
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
app.add_middleware(LoggingMiddleware)

# ---------------------------------------------------------------------------
# Static files (frontend)
# ---------------------------------------------------------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# ---------------------------------------------------------------------------
# Global exception handler
# ---------------------------------------------------------------------------
global_exception_handler(app)


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
<<<<<<< HEAD
>>>>>>> 8ee2b4665817a3550d1895555cb83836724637f7
=======
>>>>>>> ea3141f4e13ba1afa5fb4513ad9ddaf7245c89d2
>>>>>>> 1cbf00331909a46a54aae8247e9731cb55397e45
