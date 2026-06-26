"""
core/mongo.py

MongoDB Atlas connection for notification-service.

"""

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.settings import get_settings

settings = get_settings()

# ── Client (created once, reused) ────────────────────────
# Motor manages a connection pool internally.
# One client for the whole app — same as SQLAlchemy engine.
_client: AsyncIOMotorClient | None = None


def get_client() -> AsyncIOMotorClient:
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(
            settings.mongodb_url
        )
    return _client


def get_database() -> AsyncIOMotorDatabase:
    return get_client()[settings.mongodb_db_name]


# ── FastAPI dependency ────────────────────────────────────
# Use in routers: db: AsyncIOMotorDatabase = Depends(get_mongo_db)
async def get_mongo_db() -> AsyncIOMotorDatabase:
    return get_database()


# ── Lifecycle ─────────────────────────────────────────────
async def connect_mongo():
    client = get_client()
    # ping to verify connection — this is also where auth/network errors surface
    await client.admin.command("ping")
    print("✅ MongoDB Atlas connected")


async def close_mongo():
    global _client
    if _client:
        _client.close()
        _client = None
        print("🛑 MongoDB Atlas disconnected")