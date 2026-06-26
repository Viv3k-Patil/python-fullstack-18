"""
main.py — booking-service entry point

"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import get_settings
from app.routers import health, booking, booking_history

from app.core.cache import connect_redis, close_redis, get_redis
import redis.asyncio as redis
from app.core.locks import booking_lock
import asyncio
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ── Startup ──────────────────────────────────────────
    print(f"🚀 Starting {settings.app_name} v{settings.app_version} [{settings.app_env}]")
    await connect_redis()
    yield

    # ── Shutdown ─────────────────────────────────────────
    await close_redis()
    print(f"🛑 Shutting down {settings.app_name}")


app = FastAPI(
    title="MockReady — Booking Service",
    description="Manages booking requests, availability, and related operations.",
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
app.include_router(booking.router, prefix="/api/v1")
app.include_router(booking_history.router, prefix="/api/v1")

@app.get("/lock-test")
async def lock_test(redis: redis.Redis = Depends(get_redis)):

    async with booking_lock(redis, "test-resource"):
        print("🔒 LOCK ACQUIRED")

        await asyncio.sleep(5)   # simulate long operation

        print("✅ WORK DONE")

    return {"status": "done"}

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