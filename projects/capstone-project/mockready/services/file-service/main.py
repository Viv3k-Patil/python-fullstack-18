"""
main.py — file-service entry point

"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import get_settings
<<<<<<< HEAD
<<<<<<< HEAD
from app.routes import health
=======
from app.routers import health
>>>>>>> 1f68b2b4fcb50f3e1492c1817592d35670c583e5
=======
from app.routers import health,file_metadata
>>>>>>> origin/main

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ── Startup ──────────────────────────────────────────
    print(f"🚀 Starting {settings.app_name} v{settings.app_version} [{settings.app_env}]")

    yield

    # ── Shutdown ─────────────────────────────────────────
    print(f"🛑 Shutting down {settings.app_name}")


app = FastAPI(
<<<<<<< HEAD
    title="MockReady — file Service",
    description="Manages students, trainers, campuses and batches.",
=======
    title="MockReady — File Service",
    description="Manages file uploads, downloads, and related operations.",
>>>>>>> 1f68b2b4fcb50f3e1492c1817592d35670c583e5
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
<<<<<<< HEAD

<<<<<<< HEAD
=======
=======
app.include_router(file_metadata.router)
>>>>>>> origin/main

>>>>>>> 1f68b2b4fcb50f3e1492c1817592d35670c583e5
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