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

from uuid import UUID
from fastapi import APIRouter, HTTPException, Query
from app.services.booking_history_service import booking_history_service
from app.schemas.booking_history import BookingHistoryCreate, BookingHistoryUpdate
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException

router = APIRouter(
    prefix="/booking-history",
    tags=["Booking History"],
)


@router.post("", status_code=201)
async def create_booking_history(data: BookingHistoryCreate):
    try:
        booking = booking_history_service.create(data)

        return success(
            data=booking.model_dump(),
            message="Booking history created successfully",
        )

    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)


@router.get("")
async def list_booking_history(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
):
    bookings, total = booking_history_service.get_all(
        page=page,
        size=size,
    )

    return paginated(
        data=[b.model_dump() for b in bookings],
        total=total,
        page=page,
        size=size,
        message="Booking history retrieved successfully",
    )


@router.get("/{booking_history_id}")
async def get_booking_history(booking_history_id: UUID):
    try:
        booking = booking_history_service.get_by_id(booking_history_id)

        return success(
            data=booking.model_dump(),
            message="Booking history retrieved successfully",
        )

    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.put("/{booking_history_id}")
async def update_booking_history(
    booking_history_id: UUID,
    data: BookingHistoryUpdate,
):
    try:
        booking = booking_history_service.update(
            booking_history_id,
            data,
        )

        return success(
            data=booking.model_dump(),
            message="Booking history updated successfully",
        )

    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.delete("/{booking_history_id}")
async def delete_booking_history(booking_history_id: UUID):
    try:
        booking_history_service.delete(booking_history_id)

        return success(
            data=None,
            message="Booking history deleted successfully",
        )

    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)