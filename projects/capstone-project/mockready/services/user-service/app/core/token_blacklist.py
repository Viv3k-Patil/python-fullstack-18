import redis.asyncio as redis


async def blacklist_token(redis_client: redis.Redis, jti: str, ttl_seconds: int):
    await redis_client.setex(
        name=f"blacklist:{jti}",
        time=ttl_seconds,
        value="1",
    )


async def is_blacklisted(redis_client: redis.Redis, jti: str) -> bool:
    return await redis_client.exists(f"blacklist:{jti}") == 1