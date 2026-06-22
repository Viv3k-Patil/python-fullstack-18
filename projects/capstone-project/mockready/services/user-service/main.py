"""
main.py — user-service entry point

"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import get_settings
from app.routers import health, campus, batch, cabin, trainer_profile
from app.routers import trainer_availability, student_profile, trainer_campus, user
from app.core.cache import connect_redis, close_redis, get_redis
import redis.asyncio as redis
from app.core.token_blacklist import blacklist_token, is_blacklisted
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
app.include_router(batch.router, prefix="/api/v1")
app.include_router(cabin.router, prefix="/api/v1")
app.include_router(trainer_profile.router, prefix="/api/v1")
app.include_router(trainer_availability.router, prefix="/api/v1")
app.include_router(student_profile.router, prefix="/api/v1")
app.include_router(trainer_campus.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
@app.get("/", tags=["Root"])
async def root():
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "docs": "/docs",
        "health": "/health",
    }

@app.get("/blacklist-test")
async def test_blacklist(redis: redis.Redis = Depends(get_redis)):
    jti = "test-token"

    # blacklist for 60 seconds
    await blacklist_token(redis, jti, 60)

    is_blocked = await is_blacklisted(redis, jti)

    return {
        "blacklisted": is_blocked
    }

@app.get("/cache-test")
async def cache_test(redis: redis.Redis = Depends(get_redis)):
    from app.core.cache_helpers import get_cached, set_cached

    key = "cache:test"

    cached = await get_cached(redis, key)
    if cached:
        return {"source": "cache", "data": cached}

    data = {"name": "vivek"}

    await set_cached(redis, key, data, 30)

    return {"source": "db", "data": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.is_development,
        log_level="debug" if settings.debug else "info",
    )