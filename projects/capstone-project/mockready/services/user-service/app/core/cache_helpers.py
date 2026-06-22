import json
from typing import Any
import redis.asyncio as redis


async def get_cached(redis_client: redis.Redis, key: str) -> Any | None:
    """Get value from cache. Returns None if not found."""
    value = await redis_client.get(key)
    if value is None:
        return None
    return json.loads(value)


async def set_cached(
    redis_client: redis.Redis,
    key: str,
    value: Any,
    ttl_seconds: int,
):
    """Store value in cache with TTL."""
    await redis_client.setex(
        name=key,
        time=ttl_seconds,
        value=json.dumps(value, default=str),
    )


async def invalidate(redis_client: redis.Redis, key: str):
    """Delete a specific cache key."""
    await redis_client.delete(key)