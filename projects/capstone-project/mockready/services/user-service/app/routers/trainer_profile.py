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

from fastapi import APIRouter, HTTPException, Query
from app.schemas.trainer_profile import TrainerProfileCreate, TrainerProfileUpdate, TrainerProfileResponse
from app.services.trainer_profile_service import TrainerProfileService  
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException    
from app.core.database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/trainer-profiles", tags=["Trainer Profiles"])


@router.post("", status_code=201)
async def create_trainer_profile(data: TrainerProfileCreate, db: AsyncSession = Depends(get_db)):
    try:
        trainer_profile = await TrainerProfileService(db).create(data)
        return success(
            data=trainer_profile.model_dump() ,
            message="Trainer profile created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)
    

@router.get("")
async def list_trainer_profiles(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_db)
):
    trainer_profiles, total = await TrainerProfileService(db).get_all(page=page, size=size)
    return paginated(
        data=[tp.model_dump() for tp in trainer_profiles],
        total=total,
        page=page,
        size=size,
        message="Trainer profiles retrieved successfully",
    )      
@router.get("/{trainer_id}")
async def get_trainer_profile(trainer_id: int, db: AsyncSession = Depends(get_db)):
    try:
        trainer_profile = await TrainerProfileService(db).get_by_trainer_id(trainer_id)
        return success(
            data=trainer_profile.model_dump(),
            message="Trainer profile retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
    
@router.put("/{trainer_id}")
async def update_trainer_profile(trainer_id: int, data: TrainerProfileUpdate, db: AsyncSession = Depends(get_db)):
    try:
        trainer_profile = await TrainerProfileService(db).update(trainer_id, data)
        return success(
            data=trainer_profile.model_dump(),
            message="Trainer profile updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

@router.delete("/{trainer_id}", status_code=204)
async def delete_trainer_profile(trainer_id: int, db: AsyncSession = Depends(get_db)):
    try:
      is_deleted = await TrainerProfileService(db).delete(trainer_id)    
      return success(
          data={"deleted": is_deleted},
          message="Trainer profile deleted successfully",
      )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
