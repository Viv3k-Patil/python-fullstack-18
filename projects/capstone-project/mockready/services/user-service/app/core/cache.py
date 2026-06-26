"""
core/cache.py

Redis client wrapper.
One connection pool shared across the whole service.
"""

import redis.asyncio as redis
from app.core.settings import get_settings

settings = get_settings()

# ── Single client instance ────────────────────────────────
_redis_client: redis.Redis | None = None


def get_redis_client() -> redis.Redis:
    global _redis_client

    if _redis_client is None:
        _redis_client = redis.from_url(
            settings.redis_url,   # 🔥 your rediss:// URL
            encoding="utf-8",
            decode_responses=True,
            max_connections=20,
        )

    return _redis_client


# ── FastAPI dependency ────────────────────────────────────
async def get_redis() -> redis.Redis:
    return get_redis_client()


# ── Lifecycle ─────────────────────────────────────────────
async def connect_redis():
    client = get_redis_client()
    await client.ping()   # 🔥 THIS WILL TEST CONNECTION
    print("✅ Redis connected")


async def close_redis():
    global _redis_client

    if _redis_client:
        await _redis_client.aclose()
        _redis_client = None
        print("🛑 Redis disconnected")