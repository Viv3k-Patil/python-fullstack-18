import redis.asyncio as redis


class RedisLock:

    def __init__(self, redis_client: redis.Redis, key: str, ttl_seconds: int = 10):
        self.redis = redis_client
        self.key = key
        self.ttl = ttl_seconds

    async def acquire(self) -> bool:
        result = await self.redis.set(
            name=self.key,
            value="1",
            nx=True,   # 🔥 only set if NOT exists
            ex=self.ttl,  # auto expire
        )
        return result is not None

    async def release(self):
        await self.redis.delete(self.key)

    async def __aenter__(self):
        acquired = await self.acquire()
        if not acquired:
            raise Exception("Resource is locked. Try again.")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.release()


def booking_lock(redis_client: redis.Redis, resource_id: str) -> RedisLock:
    key = f"lock:booking:{resource_id}"
    return RedisLock(redis_client, key, ttl_seconds=10)