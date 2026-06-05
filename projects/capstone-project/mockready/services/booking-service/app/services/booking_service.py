
"""
services/booking_service.py

Business logic layer.

Responsibilities:
1. Database operations
2. Business rules
3. Data manipulation

NO HTTP logic here.
NO router logic here.
"""

from uuid import UUID
from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.schemas.booking_schemas import BookingCreate, BookingUpdate, BookingResponse


class BookingService:

    @staticmethod
    def create_booking(db: Session, payload: BookingCreate):
        booking = Booking(
            student_id=payload.student_id,
            trainer_id=payload.trainer_id,
            cabin_id=payload.cabin_id,
            campus_id=payload.campus_id,
            interview_type=payload.interview_type,
            status=payload.status
        )

        db.add(booking)
        db.commit()
        db.refresh(booking)

        return booking

    @staticmethod
    def get_all_bookings(db: Session):
        return db.query(Booking).all()

    @staticmethod
    def get_booking_by_id(db: Session, booking_id: int):
        return (
            db.query(Booking)
            .filter(Booking.id == booking_id)
            .first()
        )

    @staticmethod
    def update_booking(
        db: Session,
        booking_id: int,
        payload: BookingUpdate
    ):
        booking = (
            db.query(Booking)
            .filter(Booking.id == booking_id)
            .first()
        )

        if not booking:
            return None

        update_data = payload.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(booking, key, value)

        db.commit()
        db.refresh(booking)

        return booking

    @staticmethod
    def delete_booking(db: Session, booking_id: int):

        booking = (
            db.query(Booking)
            .filter(Booking.id == booking_id)
            .first()
        )

        if not booking:
            return None

        db.delete(booking)
        db.commit()

        return booking