from uuid import UUID, uuid4
from datetime import datetime, timezone
from fastapi import HTTPException

from app.schemas.booking_history import (
    BookingHistoryCreate,
    BookingHistoryUpdate,
    BookingHistoryResponse,
)
from app.core.exceptions import NotFoundException, ConflictException


# ── In-memory store ───────────────────────────────────────
booking_histories: dict[UUID, dict] = {}


class BookingHistoryService:

    # ── CREATE ───────────────────────────────────────────
    def create(self, data: BookingHistoryCreate) -> BookingHistoryResponse:

        booking_history = {
            "booking_history_id": uuid4(),
            "booking_id": data.booking_id,
            "trainer_id": data.trainer_id,
            "action": data.action,
            "reason": data.reason,
            "actioned_at": datetime.now(timezone.utc),
        }

        booking_histories[booking_history["booking_history_id"]] = booking_history

        return BookingHistoryResponse(**booking_history)

    # ── GET ALL ──────────────────────────────────────────
    def get_all(self, page: int, size: int) -> tuple[list[BookingHistoryResponse], int]:

        active = list(booking_histories.values())

        total = len(active)

        start = (page - 1) * size
        chunk = active[start:start + size]

        return [BookingHistoryResponse(**b) for b in chunk], total

    # ── GET BY ID ────────────────────────────────────────
    def get_by_id(self, booking_history_id: UUID) -> BookingHistoryResponse:

        booking_history = booking_histories.get(booking_history_id)

        if not booking_history:
            raise NotFoundException(f"Booking history {booking_history_id} not found")

        return BookingHistoryResponse(**booking_history)

    # ── UPDATE ───────────────────────────────────────────
    def update(self, booking_history_id: UUID, data: BookingHistoryUpdate) -> BookingHistoryResponse:

        booking_history = booking_histories.get(booking_history_id)

        if not booking_history:
            raise NotFoundException(f"Booking history {booking_history_id} not found")

        updates = data.model_dump(exclude_none=True)
        booking_history.update(updates)

        booking_histories[booking_history_id] = booking_history

        return BookingHistoryResponse(**booking_history)

    # ── DELETE (soft style like batch) ───────────────────
    def delete(self, booking_history_id: UUID) -> dict:

        booking_history = booking_histories.get(booking_history_id)

        if not booking_history:
            raise NotFoundException(f"Booking history {booking_history_id} not found")

        del booking_histories[booking_history_id]

        return {"message": "Booking history deleted successfully"}


booking_history_service = BookingHistoryService()