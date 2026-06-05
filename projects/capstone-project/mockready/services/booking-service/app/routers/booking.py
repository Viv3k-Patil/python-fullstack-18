<<<<<<< HEAD

"""
routers/booking.py

HTTP layer only.

Responsibilities:
1. Accept request
2. Validate request
3. Call service layer
4. Return response
5. Raise HTTP errors

NO business logic here.
"""


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.booking_schemas import (
    BookingCreate,
    BookingUpdate,
    BookingResponse
)
from app.services.booking_service import BookingService


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.post("/", response_model=BookingResponse)
def create_booking(
    payload: BookingCreate,
    db: Session = Depends(get_db)
):
    return BookingService.create_booking(db, payload)


@router.get("/", response_model=list[BookingResponse])
def get_all_bookings(
    db: Session = Depends(get_db)
):
    return BookingService.get_all_bookings(db)


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking_by_id(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = BookingService.get_booking_by_id(
        db,
        booking_id
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking


@router.put("/{booking_id}", response_model=BookingResponse)
def update_booking(
    booking_id: int,
    payload: BookingUpdate,
    db: Session = Depends(get_db)
):
    booking = BookingService.update_booking(
        db,
        booking_id,
        payload
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking


@router.delete("/{booking_id}")
def delete_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = BookingService.delete_booking(
        db,
        booking_id
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return {
        "message": "Booking deleted successfully"
    }
=======
"""
routers/booking.py

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

from app.schemas.booking_schemas import BookingCreate, BookingUpdate
from app.services.booking_service import BookingService
from app.core.responses import success, paginated
from app.core.exceptions import NotFoundException, ConflictException
from app.core.database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("", status_code=201)
async def create_booking(data: BookingCreate, db: AsyncSession = Depends(get_db)):
    try:
        booking = await BookingService(db).create(data)
        return success(
            data=booking,
            message="Booking created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)


@router.get("")
async def list_bookings(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_db)
):
    bookings, total = await BookingService(db).get_all(page=page, size=size)
    return paginated(
        data=[b.model_dump() for b in bookings],
        total=total,
        page=page,
        size=size,
        message="Bookings retrieved successfully",
    )


@router.get("/{booking_id}")
async def get_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    try:
        booking = await BookingService(db).get_by_id(booking_id)
        return success(
            data=booking.model_dump(),
            message="Booking retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.put("/{booking_id}")
async def update_booking(booking_id: int, data: BookingUpdate, db: AsyncSession = Depends(get_db)):
    try:
        booking = await BookingService(db).update(booking_id, data)
        return success(
            data=booking.model_dump(),
            message="Booking updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.delete("/{booking_id}")
async def delete_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    try:
        is_deleted = await BookingService(db).delete(booking_id)
        return success(
            data=is_deleted,
            message="Booking deactivated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
>>>>>>> f2524e327495094f501c0d5f9153b129834ad2cb
