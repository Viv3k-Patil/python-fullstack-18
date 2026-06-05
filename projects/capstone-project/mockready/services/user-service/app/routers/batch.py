<<<<<<< HEAD
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
from uuid import UUID
from fastapi import APIRouter, HTTPException, Query     
from app.schemas.batch import BatchCreate, BatchUpdate
from app.services.batch_service import batch_service
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException
router = APIRouter(prefix="/batches", tags=["Batches"])

@router.post("", status_code=201)
async def create_batch(data: BatchCreate):
    try:
        batch = batch_service.create(data)
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
):
    batches, total = batch_service.get_all(page=page, size=size)
    return paginated(
        data=[b.model_dump() for b in batches],
        total=total,
        page=page,
        size=size,
        message="Batches retrieved successfully",
    )
@router.get("/{batch_id}")
async def get_batch(batch_id: UUID):
    try:
        batch = batch_service.get_by_id(batch_id)
        return success(
            data=batch.model_dump(),
            message="Batch retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

@router.put("/{batch_id}")
async def update_batch(batch_id: UUID, data: BatchUpdate):
    try:
        batch = batch_service.update(batch_id, data)
        return success(
            data=batch.model_dump(),
            message="Batch updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.delete("/{batch_id}")
async def delete_batch(batch_id: UUID):
    try:
        batch = batch_service.delete(batch_id)
        return success(
            data=batch.model_dump(),
            message="Batch deleted successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

=======
from fastapi import APIRouter, Query, status
from uuid import UUID

from app.schemas.batch import BatchCreate, BatchUpdate, BatchResponse
from app.services.batch_service import batch_service

router = APIRouter(prefix="/batches", tags=["Batches"])


@router.post("", response_model=BatchResponse, status_code=status.HTTP_201_CREATED)
def create_batch(payload: BatchCreate):
    return batch_service.create(payload)


@router.get("", response_model=list[BatchResponse])
def get_all_batches(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    batches, _ = batch_service.get_all(page=page, size=size)
    return batches


@router.get("/{batch_id}", response_model=BatchResponse)
def get_batch_by_id(batch_id: UUID):
    return batch_service.get_by_id(batch_id)


@router.patch("/{batch_id}", response_model=BatchResponse)
def update_batch(batch_id: UUID, payload: BatchUpdate):
    return batch_service.update(batch_id, payload)


@router.delete("/{batch_id}", response_model=BatchResponse)
def delete_batch(batch_id: UUID):
    return batch_service.delete(batch_id)
>>>>>>> 93280eaa (Batch Created)
