from pydantic import BaseModel, Field
from uuid import UUID,uuid4
from datetime import datetime
from enum import Enum


class BookingAction(str, Enum):
    CREATED = "CREATED"
    ASSIGNED = "ASSIGNED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    RESCHEDULED = "RESCHEDULED"


class BookingHistoryCreate(BaseModel):
    booking_id: UUID
    trainer_id: UUID
    action: BookingAction
    reason: str | None = None


class BookingHistoryUpdate(BaseModel):
    booking_id: UUID | None = None
    trainer_id: UUID | None = None
    action: BookingAction | None = None
    reason: str | None = None


class BookingHistoryResponse(BaseModel):
    booking_history_id: UUID
    booking_id: UUID
    trainer_id: UUID
    action: BookingAction
    reason: str | None
    actioned_at: datetime

    model_config = {"from_attributes": True}