"""
main.py — user-service entry point

"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import get_settings
from app.routers import health, campus, batch, cabin, trainer_profile
from app.routers import trainer_availability, student_profile

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ── Startup ──────────────────────────────────────────
    print(f"🚀 Starting {settings.app_name} v{settings.app_version} [{settings.app_env}]")

    yield

    # ── Shutdown ─────────────────────────────────────────
    print(f"🛑 Shutting down {settings.app_name}")


app = FastAPI(
    title="MockReady — User Service",
    description="Manages students, trainers, admins, campuses and batches.",
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
app.include_router(campus.router, prefix="/api/v1")
app.include_router(trainer_availability.router, prefix="/api/v1")
app.include_router(batch.router, prefix="/api/v1")
app.include_router(cabin.router, prefix="/api/v1")
app.include_router(trainer_profile.router, prefix="/api/v1")
app.include_router(student_profile.router, prefix="/api/v1")

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