"""
routers/student_profile.py

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

from app.schemas.student_profile import StudentProfileCreate, StudentProfileUpdate
from app.services.student_profile_service import Student_Profile_Service
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException


router = APIRouter(
    prefix="/student-profile",
    tags=["Student Profile"]
)

@router.post("", status_code=201)
async def create_student_profile(data: StudentProfileCreate):
    try:
        profile = Student_Profile_Service().create(data)

        return success(
            data=profile.model_dump(),
            message="Student profile created successfully",
        )

    except ConflictException as e:
        raise HTTPException(
            status_code=409,
            detail=e.message
        )

@router.get("")
async def list_student_profiles(    
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
):
    service = Student_Profile_Service()
    profiles, total = service.get_all(page=page, size=size)
    return paginated(
        data=[p.model_dump() for p in profiles],
        total=total,
        page=page,
        size=size,
        message="Student profiles retrieved successfully",
    )
    
@router.get("/{student_id}")
async def get_student_profile(student_id: UUID):
    try:
        profile = Student_Profile_Service().get_by_id(student_id)
        return success(
            data=profile.model_dump(),
            message="Student profile retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )
    
@router.put("/{student_id}")
async def update_student_profile(student_id: UUID, data: StudentProfileUpdate):
    try:
        profile = Student_Profile_Service().update(student_id, data)
        return success(
            data=profile.model_dump(),
            message="Student profile updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )
    
@router.delete("/{student_id}")
async def delete_student_profile(student_id: UUID):
    try:
        profile = Student_Profile_Service().delete(student_id)
        return success(
            data=profile.model_dump(),
            message="Student profile deactivated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.message
        )   
