from motor.motor_asyncio import AsyncIOMotorDatabase

from app.schemas.notification import NotificationCreate, NotificationResponse
from app.repositories.notification_repository import NotificationRepository
from app.core.responses import paginated


class NotificationService:

    def __init__(self, db: AsyncIOMotorDatabase):
        self.repo = NotificationRepository(db)

    async def create(self, data: NotificationCreate) -> NotificationResponse:
        return await self.repo.create(data)

    async def get_for_user(self, user_id: int, page: int, size: int):
        notifications, total = await self.repo.get_by_user(user_id, page, size)
        return paginated(
            data=[n.model_dump() for n in notifications],
            total=total,
            page=page,
            size=size,
            message="Notifications retrieved",
        )

    async def mark_read(self, notification_id: str, user_id: int) -> bool:
        return await self.repo.mark_read(notification_id, user_id)

    async def mark_all_read(self, user_id: int) -> int:
        return await self.repo.mark_all_read(user_id)

    async def unread_count(self, user_id: int) -> int:
        return await self.repo.unread_count(user_id)