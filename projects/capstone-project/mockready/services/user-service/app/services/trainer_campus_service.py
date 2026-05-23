"""
services/trainer_campus_service.py

All business logic lives here. NEVER in the router.

The router calls this. This calls the repository (Phase 2).
When we switch to Postgres in Phase 2 — only this file
changes. The router stays exactly the same.
That is the entire point of this layer.
"""

from uuid import UUID, uuid4

from app.schemas.trainer_campus import (
    Trainer_CampusCreate,
    Trainer_CampusUpdate,
    Trainer_CampusResponse
)

from app.core.exceptions import (
    NotFoundException,
    ConflictException
)

# ── Temporary in-memory store ─────────────────────────────
# Replaced 100% by Trainer_Campus_Repository in Phase 2.
# Do not add any logic that depends on this being a dict.
_trainer_campus_service: dict[UUID, dict] = {}


class Trainer_Campus_Service:

    def create(self, data: Trainer_CampusCreate) -> Trainer_CampusResponse:

        # business rule:
        # same trainer cannot be mapped to same campus twice

        for trainer_campus in _trainer_campus_service.values():

            if (
                trainer_campus["trainer_id"] == data.trainer_id
                and trainer_campus["campus_id"] == data.campus_id
            ):
                raise ConflictException(
                    "Trainer campus mapping already exists"
                )

        trainer_campus = {
            "trainer_campus_id": uuid4(),
            "trainer_id": data.trainer_id,
            "campus_id": data.campus_id
        }

        _trainer_campus_service[
            trainer_campus["trainer_campus_id"]
        ] = trainer_campus

        return Trainer_CampusResponse(**trainer_campus)

    def get_all(self):

        return [
            Trainer_CampusResponse(**trainer_campus)
            for trainer_campus in _trainer_campus_service.values()
        ]

    def get_by_id(
        self,
        trainer_campus_id: UUID
    ) -> Trainer_CampusResponse:

        trainer_campus = _trainer_campus_service.get(
            trainer_campus_id
        )

        if not trainer_campus:
            raise NotFoundException(
                f"Trainer campus {trainer_campus_id} not found"
            )

        return Trainer_CampusResponse(**trainer_campus)

    def update(
        self,
        trainer_campus_id: UUID,
        data: Trainer_CampusUpdate
    ) -> Trainer_CampusResponse:

        trainer_campus = _trainer_campus_service.get(
            trainer_campus_id
        )

        if not trainer_campus:
            raise NotFoundException(
                f"Trainer campus {trainer_campus_id} not found"
            )

        updates = data.model_dump(exclude_none=True)

        trainer_campus.update(updates)

        _trainer_campus_service[
            trainer_campus_id
        ] = trainer_campus

        return Trainer_CampusResponse(**trainer_campus)

    def delete(self, trainer_campus_id: UUID):

        trainer_campus = _trainer_campus_service.get(
            trainer_campus_id
        )

        if not trainer_campus:
            raise NotFoundException(
                f"Trainer campus {trainer_campus_id} not found"
            )

        del _trainer_campus_service[trainer_campus_id]

        return {
            "message": "Trainer campus deleted successfully"
        }


trainer_campus_service = Trainer_Campus_Service()  