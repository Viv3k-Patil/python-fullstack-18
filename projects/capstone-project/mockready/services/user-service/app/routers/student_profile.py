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

from fastapi import APIRouter, HTTPException, Query
from app.schemas.student_profile import StudentProfileCreate, StudentProfileUpdate
from app.services.student_profile_service import StudentProfileService  
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException
from app.core.database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/student_profiles", tags=["Student Profiles"])

@router.post("", status_code=201)
async def create_student_profile(data: StudentProfileCreate, db: AsyncSession = Depends(get_db)):
    try:
        student_profile = await StudentProfileService(db).create(data)
        return success(
            data=student_profile,
            message="Student profile created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)

@router.get("")
async def list_student_profiles(    
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_db)
):
    student_profiles, total = await StudentProfileService(db).get_all(page=page, size=size)
    return paginated(
        data=[sp.model_dump() for sp in student_profiles],
        total=total,
        page=page,
        size=size,
        message="Student profiles retrieved successfully",
    )

@router.get("/{student_profile_id}")
async def get_student_profile(student_profile_id: int, db: AsyncSession = Depends(get_db)):
    try:
        student_profile = await StudentProfileService(db).get_by_id(student_profile_id)
        return success(
            data=student_profile.model_dump(),
            message="Student profile retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message) 


@router.put("/{student_profile_id}")
async def update_student_profile(student_profile_id: int, data: StudentProfileUpdate, db: AsyncSession = Depends(get_db)):
    try:
        student_profile = await StudentProfileService(db).update(student_profile_id, data)
        return success(
            data=student_profile,
            message="Student profile updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)  
    

@router.delete("/{student_profile_id}", status_code=204)
async def delete_student_profile(student_profile_id: int, db: AsyncSession = Depends(get_db)):
    try:
       is_deleted = await StudentProfileService(db).delete(student_profile_id)
       return success(
            data= is_deleted,
            message="Student profile deleted successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)