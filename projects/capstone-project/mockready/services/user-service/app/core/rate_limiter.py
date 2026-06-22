import time
import redis.asyncio as redis
from fastapi import HTTPException


class RateLimiter:

    def __init__(self, redis_client: redis.Redis, limit: int, window_seconds: int = 60):
        self.redis = redis_client
        self.limit = limit
        self.window = window_seconds

    async def check(self, identifier: str):
        """
        identifier = user_id OR IP
        """

        # current time window
        window_start = int(time.time()) // self.window

        key = f"ratelimit:{identifier}:{window_start}"

        # increment counter
        count = await self.redis.incr(key)

        # set expiry only first time
        if count == 1:
            await self.redis.expire(key, self.window)

        if count > self.limit:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Try again later."
            )

        return count