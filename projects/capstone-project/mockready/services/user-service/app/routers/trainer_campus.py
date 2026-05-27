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
    TrainerCampusCreate,
    TrainerCampusUpdate
)   
from app.services.trainer_campus_service import (
    Trainer_Campus_Service 
)
from app.core.responses import paginated, success  
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
    data: TrainerCampusCreate
):
    try:
        trainer_campus = Trainer_Campus_Service().create(data)

        return success(
            data=trainer_campus.model_dump(),
            message="Trainer campus assignment created successfully",
        )

    except ConflictException as e:
        raise HTTPException(
            status_code=409,
            detail=e.message
        )
    
@router.get("")
async def list_trainer_campuses(    
    page: int = 1,
    size: int = 20,
):
    service = Trainer_Campus_Service()
    trainer_campuses, total = service.get_all(page=page, size=size)
    return paginated(
        data=[tc.model_dump() for tc in trainer_campuses],
        total=total,
        page=page,
        size=size,
        message="Trainer campus assignments retrieved successfully",
    )
    

@router.get("/{trainer_campus_id}")
async def get_trainer_campus(trainer_campus_id: UUID):
    try:
        trainer_campus = Trainer_Campus_Service().get_by_id(trainer_campus_id)

        return success(
            data=trainer_campus.model_dump(),
            message="Trainer campus assignment retrieved successfully",
        )

    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )
    
@router.put("/{trainer_campus_id}")
async def update_trainer_campus(
    trainer_campus_id: UUID,
    data: TrainerCampusUpdate
):
    try:
        updated_trainer_campus = Trainer_Campus_Service().update(trainer_campus_id, data)

        return success(
            data=updated_trainer_campus.model_dump(),
            message="Trainer campus assignment updated successfully",
        )

    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )
    except ConflictException as e:
        raise HTTPException(
            status_code=409,
            detail=e.message
        )
    
@router.delete("/{trainer_campus_id}")
async def delete_trainer_campus(trainer_campus_id: UUID):
    try:
        trainer_campus = Trainer_Campus_Service().delete(trainer_campus_id)
        return success(
            data=trainer_campus.model_dump(),
            message="Trainer campus assignment deactivated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
        


