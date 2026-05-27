# services/booking_service.py

"""
All business logic lives here. NEVER in the router.

The router calls this. This calls the repository (Phase 2).
When we switch to Postgres in Phase 2 — only this file
changes. The router stays exactly the same.
That is the entire point of this layer.
"""


from datetime import datetime, timezone

from app.schemas.booking_schemas import (
    BookingCreate,
    BookingUpdate,
    BookingResponse
)
from app.core.exceptions import (
    NotFoundException,
    ConflictException
)

# ── Temporary in-memory store ─────────────────────────────
# Replaced 100% by BookingRepository in Phase 2.
# Do not add any logic that depends on this being a dict.
_bookings: dict[int, dict] = {}


class BookingService:

    def create(self, data: BookingCreate) -> BookingResponse:

        # business rule:
        # same student cannot book same slot twice
        for booking in _bookings.values():

            if (
                booking["student_id"] == data.student_id
                and booking["slot_time"] == data.slot_time
                and booking["is_active"]
            ):
                raise ConflictException(
                    "Booking already exists for this slot"
                )

        booking = {
            "id": int,
            "student_id": data.student_id,
            "campus_id": data.campus_id,
            "interviewer_id": data.interviewer_id,
            "slot_time": data.slot_time,
            "status": "scheduled",
            "feedback": None,
            "score": None,
            "is_active": True,
            "created_at": datetime.now(timezone.utc),
        }

        _bookings[booking["id"]] = booking

        return BookingResponse(**booking)

    def get_all(
        self,
        page: int,
        size: int
    ) -> tuple[list[BookingResponse], int]:

        active = [
            booking
            for booking in _bookings.values()
            if booking["is_active"]
        ]

        total = len(active)

        start = (page - 1) * size

        chunk = active[start: start + size]

        return (
            [BookingResponse(**booking) for booking in chunk],
            total
        )

    def get_by_id(self, booking_id: int) -> BookingResponse:

        booking = _bookings.get(booking_id)

        if not booking or not booking["is_active"]:
            raise NotFoundException(
                f"Booking {booking_id} not found"
            )

        return BookingResponse(**booking)

    def update(
        self,
        booking_id: int,
        data: BookingUpdate
    ) -> BookingResponse:

        booking = _bookings.get(booking_id)

        if not booking or not booking["is_active"]:
            raise NotFoundException(
                f"Booking {booking_id} not found"
            )

        # only update fields client sent
        updates = data.model_dump(exclude_none=True)

        booking.update(updates)

        _bookings[booking_id] = booking

        return BookingResponse(**booking)

    def delete(self, booking_id:int) -> BookingResponse:

        booking = _bookings.get(booking_id)

        if not booking or not booking["is_active"]:
            raise NotFoundException(
                f"Booking {booking_id} not found"
            )

        # soft delete only
        booking["is_active"] = False

        return BookingResponse(**booking)