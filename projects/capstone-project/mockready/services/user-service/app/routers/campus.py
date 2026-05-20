"""
routers/campus.py

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

from app.schemas.campus import CampusCreate, CampusUpdate
from app.services.campus_service import campus_service
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException

router = APIRouter(prefix="/campuses", tags=["Campuses"])


@router.post("", status_code=201)
async def create_campus(data: CampusCreate):
    try:
        campus = campus_service.create(data)
        return success(
            data=campus.model_dump(),
            message="Campus created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)


@router.get("")
async def list_campuses(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
):
    campuses, total = campus_service.get_all(page=page, size=size)
    return paginated(
        data=[c.model_dump() for c in campuses],
        total=total,
        page=page,
        size=size,
        message="Campuses retrieved successfully",
    )


@router.get("/{campus_id}")
async def get_campus(campus_id: UUID):
    try:
        campus = campus_service.get_by_id(campus_id)
        return success(
            data=campus.model_dump(),
            message="Campus retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.put("/{campus_id}")
async def update_campus(campus_id: UUID, data: CampusUpdate):
    try:
        campus = campus_service.update(campus_id, data)
        return success(
            data=campus.model_dump(),
            message="Campus updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.delete("/{campus_id}")
async def delete_campus(campus_id: UUID):
    try:
        campus = campus_service.delete(campus_id)
        return success(
            data=campus.model_dump(),
            message="Campus deactivated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)