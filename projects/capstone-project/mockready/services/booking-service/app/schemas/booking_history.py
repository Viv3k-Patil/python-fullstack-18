"""
schemas/booking_history.py
"""

from pydantic import BaseModel, Field
from datetime import date


class BookingHistoryCreate(BaseModel):
    booking_id: int
    trainer_id: int
    action_data: str = Field(..., max_length=100)
    reason: str
    actioned_at: date


class BookingHistoryUpdate(BaseModel):
    action_data: str | None = Field(None, max_length=100)
    reason: str | None = None
    actioned_at: date | None = None


class BookingHistoryResponse(BaseModel):
    booking_history_id: int
    booking_id: int
    trainer_id: int
    action_data: str
    reason: str
    actioned_at: date

    model_config = {"from_attributes": True} 