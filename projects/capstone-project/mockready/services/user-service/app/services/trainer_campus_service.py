"""
services/Trainer_Campus_Service.py

All business logic lives here. NEVER in the router.

The router calls this. This calls the repository (Phase 2).
When we switch to Postgres in Phase 2 — only this file
changes. The router stays exactly the same.
That is the entire point of this layer.
"""

from uuid import UUID, uuid4
from datetime import datetime, timezone     
from app.schemas.trainer_campus import TrainerCampusCreate, TrainerCampusUpdate, TrainerCampusResponse
from app.core.exceptions import NotFoundException, ConflictException
# ── Temporary in-memory store ─────────────────────────────
# Replaced 100% by Trainer_Campus_ServiceRepository in Phase 2.

_trainer_campus_service: dict[UUID, dict] = {}

class Trainer_Campus_Service:
    def create(self, data: TrainerCampusCreate) -> TrainerCampusResponse:
        # business rule: same trainer cannot be assigned to the same campus more than once
        for tc in _trainer_campus_service.values():
            if tc["trainer_id"] == data.trainer_id and tc["campus_id"] == data.campus_id:
                raise ConflictException("Trainer is already assigned to this campus")
        
        trainer_campus = {
            "id": uuid4(),
            "campus_id": data.campus_id,
            "trainer_id": data.trainer_id,
            "location": data.location,
            "capacity": data.capacity,
            "is_active": True,
            "created_at": datetime.now(timezone.utc)
        }
        _trainer_campus_service[trainer_campus["id"]] = trainer_campus

        return TrainerCampusResponse(**trainer_campus)
    
    def get_all(self, page: int, size: int) -> tuple[list[TrainerCampusResponse], int]:
        active = [t for t in _trainer_campus_service.values() if t["is_active"]]
        total = len(active)
        start = (page - 1) * size
        chunk = active[start: start + size]
        return [TrainerCampusResponse(**t) for t in chunk], total   
    

    def get_by_id(self, trainer_campus_id: UUID) -> TrainerCampusResponse:
        trainer_campus = _trainer_campus_service.get(trainer_campus_id)
        if not trainer_campus:
            raise NotFoundException("Trainer campus assignment not found")
        return TrainerCampusResponse(**trainer_campus)
    

    def update(self, trainer_campus_id: UUID, data: TrainerCampusUpdate) -> TrainerCampusResponse:
        trainer_campus = _trainer_campus_service.get(trainer_campus_id)
        if not trainer_campus:
            raise NotFoundException("Trainer campus assignment not found")
        
        # business rule: same trainer cannot be assigned to the same campus more than once
        for tc_id, tc in _trainer_campus_service.items():
            if (
                tc_id != trainer_campus_id and
                tc["trainer_id"] == (data.trainer_id or trainer_campus["trainer_id"]) and
                tc["campus_id"] == (data.campus_id or trainer_campus["campus_id"])
            ):
                raise ConflictException("Trainer is already assigned to this campus")
        
        updated_trainer_campus = {
            **trainer_campus,
            **data.model_dump(exclude_none=True)  # only update fields that are provided
        }
        _trainer_campus_service[trainer_campus_id] = updated_trainer_campus

        return TrainerCampusResponse(**updated_trainer_campus)
    
    def delete(self, trainer_campus_id: UUID) -> TrainerCampusResponse:
        trainer_campus = _trainer_campus_service.get(trainer_campus_id)
        if not trainer_campus:
            raise NotFoundException("Trainer campus assignment not found")

        # always soft delete — never remove from DB
        trainer_campus["is_active"] = False
        return TrainerCampusResponse(**trainer_campus)
    
trainer_campus_service = Trainer_Campus_Service()