
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

"""
main.py — file-service entry point

"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import get_settings
from app.routers import health

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ── Startup ──────────────────────────────────────────
    print(f"🚀 Starting {settings.app_name} v{settings.app_version} [{settings.app_env}]")

    yield

    # ── Shutdown ─────────────────────────────────────────
    print(f"🛑 Shutting down {settings.app_name}")


app = FastAPI(
    title="MockReady — File Service",
    description="Manages file uploads, downloads, and related operations.",
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# ── Middleware ────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.is_development else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ──────────────────────────────────────────────
app.include_router(health.router)


@app.get("/", tags=["Root"])
async def root():
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "docs": "/docs",
        "health": "/health",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.is_development,
        log_level="debug" if settings.debug else "info",

    )

