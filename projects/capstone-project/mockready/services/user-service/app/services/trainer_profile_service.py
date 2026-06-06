"""
services/trainer_profile_service.py

All business logic lives here. NEVER in the router.

The router calls this. This calls the repository (Phase 2).
When we switch to Postgres in Phase 2 — only this file
changes. The router stays exactly the same.
That is the entire point of this layer.
"""

from uuid import UUID, uuid4
from datetime import datetime, timezone

from app.schemas.trainer_profile import TrainerCreate, TrainerUpdate, TrainerResponse
from app.core.exceptions import NotFoundException, ConflictException

# ── Temporary in-memory store ─────────────────────────────
# Replaced 100% by TrainerRepository in Phase 2.
# Do not add any logic that depends on this being a dict.
_trainers: dict[UUID, dict] = {}


class TrainerService:

    def create(self, data: TrainerCreate) -> TrainerResponse:
        # business rule: no duplicate trainer names
        for t in _trainers.values():
            if t["name"].lower() == data.name.lower():
                raise ConflictException(f"Trainer '{data.name}' already exists")

        trainer = {
            "id": uuid4(),
            "name": data.name,
            "city": data.city,
            "address": data.address,
            "experience_years": data.experience_years,
            "skills": data.skills,
            "specialization": data.specialization,
            "rating": data.rating,
            "is_active": True,
            "created_at": datetime.now(timezone.utc),
        }
        _trainers[trainer["id"]] = trainer
        return TrainerResponse(**trainer)

    def get_all(self, page: int, size: int) -> tuple[list[TrainerResponse], int]:
        active = [t for t in _trainers.values() if t["is_active"]]
        total = len(active)
        start = (page - 1) * size
        chunk = active[start: start + size]
        return [TrainerResponse(**t) for t in chunk], total

    def get_by_id(self, trainer_id: UUID) -> TrainerResponse:
        trainer = _trainers.get(trainer_id)
        if not trainer or not trainer["is_active"]:
            raise NotFoundException(f"Trainer {trainer_id} not found")
        return TrainerResponse(**trainer)

    def update(self, trainer_id: UUID, data: TrainerUpdate) -> TrainerResponse:
        trainer = _trainers.get(trainer_id)
        if not trainer or not trainer["is_active"]:
            raise NotFoundException(f"Trainer {trainer_id} not found")

        # only update fields the client actually sent
        updates = data.model_dump(exclude_none=True)
        trainer.update(updates)
        _trainers[trainer_id] = trainer
        return TrainerResponse(**trainer)

    def delete(self, trainer_id: UUID) -> TrainerResponse:
        trainer = _trainers.get(trainer_id)
        if not trainer or not trainer["is_active"]:
            raise NotFoundException(f"Trainer {trainer_id} not found")

        # always soft delete — never remove from DB
        trainer["is_active"] = False
        return TrainerResponse(**trainer)


trainer_service = TrainerService()