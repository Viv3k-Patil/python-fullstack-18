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