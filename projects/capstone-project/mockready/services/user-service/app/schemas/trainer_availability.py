from pydantic import BaseModel, Field
from datetime import datetime, time, date


class TrainerAvailabilityCreate(BaseModel):
    trainer_id: int = Field(..., ge=1)
    date: date
    start_time: time
    end_time: time
    is_booked: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TrainerAvailabilityUpdate(BaseModel):
    trainer_id: int | None = None
    date: date | None = None
    start_time: time | None = None
    end_time: time | None = None
    is_booked: bool | None = None


class TrainerAvailabilityResponse(BaseModel):
    id: int
    trainer_id: int
    date: date
    start_time: time
    end_time: time
    is_booked: bool
    created_at: datetime

    model_config = {"from_attributes": True}