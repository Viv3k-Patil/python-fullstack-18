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

from fastapi import APIRouter, HTTPException, Query
from app.schemas.trainer_campus import TrainerCampusCreate, TrainerCampusUpdate 
from app.services.trainer_campus_service import TrainerCampusService
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException
from app.core.database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/trainer-campuses", tags=["Trainer Campuses"])

@router.post("", status_code=201)
async def create_trainer_campus(data: TrainerCampusCreate, db: AsyncSession = Depends(get_db)):
    try:
        trainer_campus = await TrainerCampusService(db).create(data)
        return success(
            data=trainer_campus,
            message="TrainerCampus created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)
    
@router.get("")
async def list_trainer_campuses(    
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_db)
):
    trainer_campuses, total = await TrainerCampusService(db).get_all(page=page, size=size)
    return paginated(
        data=[tc.model_dump() for tc in trainer_campuses],
        total=total,
        page=page,
        size=size,
        message="Trainer Campuses retrieved successfully",
    )

@router.get("/{trainer_campus_id}")
async def get_trainer_campus(trainer_campus_id: int, db: AsyncSession = Depends(get_db)):
    try:
        trainer_campus = await TrainerCampusService(db).get_by_id(trainer_campus_id)
        return success(
            data=trainer_campus.model_dump(),
            message="TrainerCampus retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
    
@router.put("/{trainer_campus_id}")
async def update_trainer_campus(trainer_campus_id: int, data: TrainerCampusUpdate, db: AsyncSession = Depends(get_db)):
    try:
        trainer_campus = await TrainerCampusService(db).update(trainer_campus_id, data)
        return success(
            data=trainer_campus,
            message="TrainerCampus updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)

@router.delete("/{trainer_campus_id}", status_code=204)
async def delete_trainer_campus(trainer_campus_id: int, db: AsyncSession = Depends(get_db)):
    try:

        is_deleted = await TrainerCampusService(db).delete(trainer_campus_id)
        return success(
            data=None,
            message="TrainerCampus deleted successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)