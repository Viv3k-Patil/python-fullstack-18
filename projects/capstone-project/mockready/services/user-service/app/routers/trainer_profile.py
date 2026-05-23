"""
routers/trainer_profile .py

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
from fastapi import APIRouter, HTTPException, Query

from app.schemas.trainer_profile import TrainerCreate, TrainerUpdate
from app.services.trainer_profile_service import trainer_service
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException

router = APIRouter(prefix="/trainers", tags=["Trainers"])


@router.post("/", status_code=201)
async def create_trainer(data: TrainerCreate):  
    try:
        trainer = trainer_service.create(data)
        return success(
            data=trainer.model_dump(),
            message="Trainer created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)


@router.get("/")
async def list_trainers(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
):
    trainers, total = trainer_service.get_all(page=page, size=size)
    return paginated(
        data=[t.model_dump() for t in trainers],
        total=total,
        page=page,
        size=size,
        message="Trainers retrieved successfully",
    )


@router.get("/{trainer_id}")
async def get_trainer(trainer_id: UUID):
    try:
        trainer = trainer_service.get_by_id(trainer_id)
        return success(
            data=trainer.model_dump(),
            message="Trainer retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.put("/{trainer_id}")
async def update_trainer(trainer_id: UUID, data: TrainerUpdate):
    try:
        trainer = trainer_service.update(trainer_id, data)
        return success(
            data=trainer.model_dump(),
            message="Trainer updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.delete("/{trainer_id}")
async def delete_trainer(trainer_id: UUID):
    try:
        trainer = trainer_service.delete(trainer_id)
        return success(
            data=trainer.model_dump(),
            message="Trainer deactivated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)