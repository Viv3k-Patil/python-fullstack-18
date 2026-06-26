from datetime import datetime, timezone
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.schemas.notification import NotificationCreate, NotificationResponse


class NotificationRepository:

    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["notifications"]

    async def create(self, data: NotificationCreate) -> NotificationResponse:
        doc = {
            "user_id": data.user_id, 
            "type": data.type,
            "title": data.title,
            "message": data.message,
            "is_read": False,
            "metadata": data.metadata,
            "created_at": datetime.now(timezone.utc),
        }
        result = await self.collection.insert_one(doc)
        doc["_id"] = result.inserted_id
        return self._to_response(doc)

    async def get_by_user(
        self,
        user_id: int,
        page: int = 1,
        size: int = 20,
    ):
        query = {"user_id": user_id}
        skip = (page - 1) * size

        total = await self.collection.count_documents(query)
        cursor = (
            self.collection
            .find(query)
            .sort("created_at", -1)
            .skip(skip)
            .limit(size)
        )
        docs = await cursor.to_list(length=size)
        return [self._to_response(d) for d in docs], total

    async def mark_read(self, notification_id: str, user_id: int) -> bool:
        result = await self.collection.update_one(
            {
                "_id": ObjectId(notification_id),
                "user_id": user_id,   
            },
            {"$set": {"is_read": True}},
        )
        return result.modified_count == 1

    async def mark_all_read(self, user_id: int) -> int:
        result = await self.collection.update_many(
            {"user_id": user_id, "is_read": False},
            {"$set": {"is_read": True}},
        )
        return result.modified_count

    async def unread_count(self, user_id: int) -> int:
        return await self.collection.count_documents(
            {"user_id": user_id, "is_read": False}
        )

    async def ensure_indexes(self):
        await self.collection.create_index("user_id")
        await self.collection.create_index("created_at")
        await self.collection.create_index([("user_id", 1), ("is_read", 1)])
        print("✅ MongoDB indexes ensured")

    def _to_response(self, doc: dict) -> NotificationResponse:
        return NotificationResponse(
            id=str(doc["_id"]),
            user_id=doc["user_id"],
            type=doc["type"],
            title=doc["title"],
            message=doc["message"],
            is_read=doc["is_read"],
            metadata=doc.get("metadata", {}),
            created_at=doc["created_at"],
        )