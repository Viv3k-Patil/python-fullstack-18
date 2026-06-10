"""
routers/user.py

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
from app.schemas.users import UserCreate, UserUpdate
from app.services.user_service import UserService
from app.core.responses import success, paginated
from app.core.exceptions import ConflictException, NotFoundException
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


router = APIRouter(prefix= "/users", tags=["Users"])

@router.post("", status_code=201)
async def create_user(data: UserCreate, db: AsyncSession = Depends(get_db)):
    try: 
        user = await UserService(db).create(data)
        return success(
          data= user,
          message = "User created successfully",

        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)
    
@router.get("")
async def list_users(
    page: int = Query(1, ge= 1, description= "Page number"),
    size: int = Query(20, ge= 1, le= 100, description= " Items per page"),
    db: AsyncSession = Depends(get_db)
):
    users, total = await UserService(db).get_all(page = page, size = size)
    return paginated(
        data = [u.model_dump() for u in users],
        total = total,
        page = page,
        size = size,
        message= "Users retrieved successfully",
    )

@router.get("/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    try:
        user = await UserService(db).get_by_id(user_id)
        return success(
            data=user.model_dump(),
            message="User retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.put("/{user_id}")
async def update_user(user_id: int, data: UserUpdate, db: AsyncSession = Depends(get_db)):
    try:
        user = await UserService(db).update(user_id, data)
        return success(
            data=user.model_dump(),
            message="User updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    try:
        is_deleted = await UserService(db).delete(user_id)
        return success(
            data=is_deleted,
            message="User deactivated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)