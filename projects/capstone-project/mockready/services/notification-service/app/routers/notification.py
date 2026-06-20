from fastapi import APIRouter, Depends, HTTPException, Query
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.schemas.notification import NotificationCreate

from app.core.mongo import get_mongo_db
from app.services.notification_service import NotificationService
from app.core.responses import success


router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("")
async def create_notification(
    payload: NotificationCreate,
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
):
    return await NotificationService(db).create(payload)


@router.get("")
async def list_notifications(
    user_id: int,
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
):
    return await NotificationService(db).get_for_user(user_id, page, size)


@router.patch("/{notification_id}/read")
async def mark_read(
    notification_id: str,
    user_id: int,
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
):
    updated = await NotificationService(db).mark_read(notification_id, user_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Notification not found")
    return success(data=None, message="Marked as read")


@router.patch("/read-all")
async def mark_all_read(
    user_id: int,
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
):
    count = await NotificationService(db).mark_all_read(user_id)
    return success(
        data={"updated": count},
        message=f"{count} notifications marked as read",
    )


@router.get("/unread-count")
async def unread_count(
    user_id: int,
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
):
    count = await NotificationService(db).unread_count(user_id)
    return success(data={"count": count}, message="Unread count retrieved")