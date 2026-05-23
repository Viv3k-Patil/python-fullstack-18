"""
schemas/trainer_campus.py

These are NOT database models.
They define what the API accepts and returns.

Rule:
  schemas/  → what the API sees   (Pydantic)
  models/   → what the DB sees    (SQLAlchemy)

trainer_campusUpdate uses all Optional fields — client sends
only what they want to change. model_dump(exclude_none=True)
strips the rest in the service layer.
"""

from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional


class Trainer_CampusCreate(BaseModel):
    trainer_id: UUID = Field(...)
    campus_id: UUID = Field(...)


class Trainer_CampusUpdate(BaseModel):
    trainer_id: UUID | None = Field(None)
    campus_id: UUID | None = Field(None)


class Trainer_CampusResponse(BaseModel):
    trainer_campus_id: UUID
    trainer_id: UUID
    campus_id: UUID

    model_config = {"from_attributes": True}