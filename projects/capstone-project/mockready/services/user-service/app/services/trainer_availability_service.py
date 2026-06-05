"""
services/Trainer_Availability_Service.py

All business logic lives here. NEVER in the router.

The router calls this. This calls the repository (Phase 2).
When we switch to Postgres in Phase 2 — only this file
changes. The router stays exactly the same.
That is the entire point of this layer.
"""

from uuid import UUID, uuid4
from datetime import datetime, timezone

from app.schemas.trainer_availability import Trainer_AvailabilityCreate, Trainer_AvailabilityUpdate, Trainer_AvailabilityResponse
from app.core.exceptions import NotFoundException, ConflictException

# ── Temporary in-memory store ─────────────────────────────
# Replaced 100% by Trainer_Availability_ServiceRepository in Phase 2.
# Do not add any logic that depends on this being a dict.
_trainer_availability_service: dict[UUID, dict] = {}


class Trainer_Availability_Service:

    def create(self, data: Trainer_AvailabilityCreate) -> Trainer_AvailabilityResponse:
        # business rule:same trainer cannot have duplicate availability
        for tavail in _trainer_availability_service.values():
            if (
                tavail["tainer_id"] == data.tainer_id
                and tavail["date"] == data.date
                and tavail["start_time"] == data.start_time
                and tavail["end_time"] == data.end_time
            ):
                raise ConflictException( "Trainer availability already exists")
            
        availability = {
            "id": uuid4(),
            "tainer_id": data.tainer_id,
            "campus_id": data.campus_id,
            "date": data.date,
            "start_time": data.start_time,
            "end_time": data.end_time,
            "is_booked": data.is_booked
        }
        _trainer_availability_service[availability["id"]] = availability

        return Trainer_AvailabilityResponse(**availability)
    
    def get_all(self):

        return [
            Trainer_AvailabilityResponse(**tavail)
            for tavail in _trainer_availability_service.values()
        ]

    def get_by_id(self,availability_id: UUID) -> Trainer_AvailabilityResponse:

        availability = _trainer_availability_service.get(availability_id)

        if not availability:
            raise NotFoundException(
                f"Trainer availability {availability_id} not found"
            )

        return Trainer_AvailabilityResponse(**availability)

    def update(self,availability_id: UUID,data: Trainer_AvailabilityUpdate) -> Trainer_AvailabilityResponse:

        availability = _trainer_availability_service.get(availability_id)

        if not availability:
            raise NotFoundException(
                f"Trainer availability {availability_id} not found"
            )

        updates = data.model_dump(exclude_none=True)

        availability.update(updates)

        _trainer_availability_service[availability_id] = availability

        return Trainer_AvailabilityResponse(**availability)

    def delete(self,availability_id: UUID):

        availability = _trainer_availability_service.get(availability_id)

        if not availability:
            raise NotFoundException(
                f"Trainer availability {availability_id} not found"
            )

        del _trainer_availability_service[availability_id]

        return {
            "message": "Trainer availability deleted successfully"
        }


trainer_availability_service = Trainer_Availability_Service()    