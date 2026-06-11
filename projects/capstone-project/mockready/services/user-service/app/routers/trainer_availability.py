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


from fastapi import APIRouter, HTTPException, Query
from app.schemas.trainer_availability import TrainerAvailabilityCreate, TrainerAvailabilityUpdate
from app.services.trainer_availability_service import TrainerAvailabilityService
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException
from app.core.database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/trainer_availabilities", tags=["Trainer Availabilities"])

@router.post("", status_code=201)
async def create_trainer_availability(data: TrainerAvailabilityCreate, db: AsyncSession = Depends(get_db)):
    try:
        availability = await TrainerAvailabilityService(db).create(data)
        return success(
            data=availability.model_dump(),
            message="Trainer availability created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)
    
@router.get("")
async def list_trainer_availabilities(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_db)
):
    availabilities, total = await TrainerAvailabilityService(db).get_all(page=page, size=size)
    return paginated(
        data=[a.model_dump() for a in availabilities],
        total=total,
        page=page,
        size=size,
        message="Trainer availabilities retrieved successfully",
    )

@router.get("/{availability_id}")
async def get_trainer_availability(availability_id: int, db: AsyncSession = Depends(get_db)):
    try:
        availability = await TrainerAvailabilityService(db).get_by_id(availability_id)
        return success(
            data=availability.model_dump(),
            message="Trainer availability retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
    
@router.put("/{availability_id}")
async def update_trainer_availability(availability_id: int, data: TrainerAvailabilityUpdate, db: AsyncSession = Depends(get_db)):
    try:
        availability = await TrainerAvailabilityService(db).update(availability_id, data)
        return success(
            data=availability.model_dump(),
            message="Trainer availability updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

    
@router.delete("/{availability_id}", status_code=204)
async def delete_trainer_availability(availability_id: int, db: AsyncSession = Depends(get_db)):
    try:
       is_deleted = await TrainerAvailabilityService(db).delete(availability_id)
       return success(
            data={"is_deleted": is_deleted},
            message="Trainer availability deleted successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)    