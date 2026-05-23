"""
routers/trainer_campus.py

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

from app.schemas.trainer_campus import (
    Trainer_CampusCreate,
    Trainer_CampusUpdate
)

from app.services.trainer_campus_service import (
    trainer_campus_service
)

from app.core.responses import success

from app.core.exceptions import (
    NotFoundException,
    ConflictException
)

router = APIRouter(
    prefix="/trainer-campus",
    tags=["Trainer Campus"]
)


@router.post("", status_code=201)
async def create_trainer_campus(
    data: Trainer_CampusCreate
):
    try:
        trainer_campus = trainer_campus_service.create(data)

        return success(
            data=trainer_campus.model_dump(),
            message="Trainer campus created successfully",
        )

    except ConflictException as e:
        raise HTTPException(
            status_code=409,
            detail=e.message
        )


@router.get("")
async def list_trainer_campus():

    trainer_campus = trainer_campus_service.get_all()

    return success(
        data=[
            tc.model_dump()
            for tc in trainer_campus
        ],
        message="Trainer campus retrieved successfully",
    )


@router.get("/{trainer_campus_id}")
async def get_trainer_campus(
    trainer_campus_id: UUID
):
    try:
        trainer_campus = trainer_campus_service.get_by_id(
            trainer_campus_id
        )

        return success(
            data=trainer_campus.model_dump(),
            message="Trainer campus retrieved successfully",
        )

    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )


@router.put("/{trainer_campus_id}")
async def update_trainer_campus(
    trainer_campus_id: UUID,
    data: Trainer_CampusUpdate
):
    try:
        trainer_campus = trainer_campus_service.update(
            trainer_campus_id,
            data
        )

        return success(
            data=trainer_campus.model_dump(),
            message="Trainer campus updated successfully",
        )

    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )


@router.delete("/{trainer_campus_id}")
async def delete_trainer_campus(
    trainer_campus_id: UUID
):
    try:
        response = trainer_campus_service.delete(
            trainer_campus_id
        )

        return success(
            data=response,
            message="Trainer campus deleted successfully",
        )

    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )