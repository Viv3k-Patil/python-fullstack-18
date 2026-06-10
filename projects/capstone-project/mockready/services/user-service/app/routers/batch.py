"""
routers/batch.py

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
from app.schemas.batch import BatchCreate, BatchUpdate
from app.services.batch_service import BatchService
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException
from app.core.database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/batches", tags=["Batches"])

@router.post("", status_code=201)
async def create_batch(data: BatchCreate ,db: AsyncSession = Depends(get_db)):
    try:
        batch = await BatchService(db).create(data)
        return success(
            data=batch.model_dump(),
            message="Batch created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)

@router.get("")
async def list_batches(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_db)
):
    batches, total = await BatchService(db).get_all(page=page, size=size)
    return paginated(
        data=[b.model_dump() for b in batches],
        total=total,
        page=page,
        size=size,
        message="Batches retrieved successfully",
    )
@router.get("/{batch_id}")
async def get_batch(batch_id: int,db : AsyncSession = Depends(get_db)):
    try:
        batch = await BatchService(db).get_by_id(batch_id)
        return success(
            data=batch.model_dump(),
            message="Batch retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

@router.put("/{batch_id}")
async def update_batch(batch_id: int, data: BatchUpdate,db : AsyncSession = Depends(get_db)):
    try:
        batch = await BatchService(db).update(batch_id, data)
        return success(
            data=batch.model_dump(),
            message="Batch updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.delete("/{batch_id}")
async def delete_batch(batch_id: int,db : AsyncSession = Depends(get_db)):
    try:
        is_deleted = await BatchService(db).delete(batch_id)
        return success(
            data=is_deleted,
            message="Batch deleted successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

