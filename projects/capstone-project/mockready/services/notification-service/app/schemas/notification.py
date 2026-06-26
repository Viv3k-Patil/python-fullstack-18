from pydantic import BaseModel
from datetime import datetime
from typing import Any


class NotificationCreate(BaseModel):
    user_id: int
    type: str
    title: str
    message: str
    metadata: dict[str, Any] = {}


class NotificationResponse(BaseModel):
    id: str
    user_id: int
    type: str
    title: str
    message: str
    is_read: bool
    metadata: dict[str, Any]
    created_at: datetime