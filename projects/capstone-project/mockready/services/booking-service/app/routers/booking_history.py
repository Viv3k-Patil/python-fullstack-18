"""
routers/booking_history.py

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

from app.schemas.booking_history import BookingHistoryCreate, BookingHistoryUpdate
from app.services.booking_history_service import BookingHistoryService
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException
from app.core.database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/booking-history", tags=["Booking History"])

@router.post("", status_code=201)
async def create_booking(data: BookingHistoryCreate, db: AsyncSession = Depends(get_db)):
    try:
        booking_history = await BookingHistoryService(db).create(data)
        return success(
            data=booking_history,
            message="Booking history created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)


@router.get("")
async def list_bookings(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_db)
):
    booking_history, total = await BookingHistoryService(db).get_all(page=page, size=size)
    return paginated(
        data=[b.model_dump() for b in booking_history],
        total=total,
        page=page,
        size=size,
        message="Booking history retrieved successfully",
    )


@router.get("/{booking_history_id}")
async def get_booking(booking_history_id: int, db: AsyncSession = Depends(get_db)):
    try:
        booking_hitory = await BookingHistoryService(db).get_by_id(booking_history_id)
        return success(
            data=booking_hitory.model_dump(),
            message="Booking history retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.put("/{booking_history_id}")
async def update_booking(booking_history_id: int, data: BookingHistoryUpdate, db: AsyncSession = Depends(get_db)):
    try:
        booking_history  = await BookingHistoryService(db).update(booking_history_id, data)
        return success(
            data=booking_history.model_dump(),
            message="Booking history updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.delete("/{booking_history_id}")
async def delete_booking(booking_history_id: int, db: AsyncSession = Depends(get_db)):
    try:
        is_deleted = await BookingHistoryService(db).delete(booking_history_id)
        return success(
            data=is_deleted,
            message="Booking history deactivated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)