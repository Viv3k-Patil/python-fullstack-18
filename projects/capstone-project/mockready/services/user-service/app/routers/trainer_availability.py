"""
routers/trainer_availability.py

HTTP layer only. Zero business logic here.

This file's only jobs:
  1. Accept and validate the request (Pydantic does this)
  2. Call the service
  3. Wrap result in response envelope
  4. Map exceptions to HTTP status codes

If you find yourself writing if/else logic here
that isn't about HTTP — move it to the service.
"""

from uuid import UUID
from fastapi import APIRouter, HTTPException

from app.schemas.trainer_availability import (
    Trainer_AvailabilityCreate,
    Trainer_AvailabilityUpdate
)

from app.services.trainer_availability_service import (
    trainer_availability_service
)

from app.core.responses import success
from app.core.exceptions import (
    NotFoundException,
    ConflictException
)

router = APIRouter(
    prefix="/trainer-availability",
    tags=["Trainer Availability"]
)


@router.post("", status_code=201)
async def create_trainer_availability(
    data: Trainer_AvailabilityCreate
):
    try:
        availability = trainer_availability_service.create(data)

        return success(
            data=availability.model_dump(),
            message="Trainer availability created successfully",
        )

    except ConflictException as e:
        raise HTTPException(
            status_code=409,
            detail=e.message
        )


@router.get("")
async def list_trainer_availability():

    availability = trainer_availability_service.get_all()

    return success(
        data=[a.model_dump() for a in availability],
        message="Trainer availability retrieved successfully",
    )


@router.get("/{availability_id}")
async def get_trainer_availability(
    availability_id: UUID
):
    try:
        availability = trainer_availability_service.get_by_id(
            availability_id
        )

        return success(
            data=availability.model_dump(),
            message="Trainer availability retrieved successfully",
        )

    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )


@router.put("/{availability_id}")
async def update_trainer_availability(
    availability_id: UUID,
    data: Trainer_AvailabilityUpdate
):
    try:
        availability = trainer_availability_service.update(
            availability_id,
            data
        )

        return success(
            data=availability.model_dump(),
            message="Trainer availability updated successfully",
        )

    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )


@router.delete("/{availability_id}")
async def delete_trainer_availability(
    availability_id: UUID
):
    try:
        response = trainer_availability_service.delete(
            availability_id
        )

        return success(
            data=response,
            message="Trainer availability deleted successfully",
        )

    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )