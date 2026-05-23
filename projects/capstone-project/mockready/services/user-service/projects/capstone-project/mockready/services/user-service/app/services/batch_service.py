from uuid import UUID, uuid4
from datetime import datetime, timezone

from app.schemas.batch import BatchCreate, BatchUpdate, BatchResponse
from app.core.exceptions import NotFoundException, ConflictException

# ── Temporary in-memory store ─────────────────────────────
# Replaced 100% by BatchRepository in Phase 2.
# Do not add any logic that depends on this being a dict.
_batches: dict[UUID, dict] = {}


class BatchService:

    def create(self, data: BatchCreate) -> BatchResponse:
        # Business rule: no duplicate batch names allowed
        for b in _batches.values():
            if b["name"].lower() == data.name.lower():
                raise ConflictException(f"Batch '{data.name}' already exists")

        batch = {
            "id": uuid4(),
            "campus_id": data.campus_id,
            "name": data.name,
            "course": data.course,
            "start_date": data.start_date,
            "end_date": data.end_date,
            "is_active": True,
            "created_at": datetime.now(timezone.utc),
        }
        _batches[batch["id"]] = batch
        return BatchResponse(**batch)

    def get_all(self, page: int, size: int) -> tuple[list[BatchResponse], int]:
        active = [b for b in _batches.values() if b["is_active"]]
        total = len(active)
        start = (page - 1) * size
        chunk = active[start: start + size]
        return [BatchResponse(**b) for b in chunk], total

    def get_by_id(self, batch_id: UUID) -> BatchResponse:
        batch = _batches.get(batch_id)
        if not batch or not batch["is_active"]:
            raise NotFoundException(f"Batch {batch_id} not found")
        return BatchResponse(**batch)

    def update(self, batch_id: UUID, data: BatchUpdate) -> BatchResponse:
        batch = _batches.get(batch_id)
        if not batch or not batch["is_active"]:
            raise NotFoundException(f"Batch {batch_id} not found")

        # Only update fields the client actually sent
        updates = data.model_dump(exclude_none=True)
        batch.update(updates)
        _batches[batch_id] = batch
        return BatchResponse(**batch)

    def delete(self, batch_id: UUID) -> BatchResponse:
        batch = _batches.get(batch_id)
        if not batch or not batch["is_active"]:
            raise NotFoundException(f"Batch {batch_id} not found")

        # Always soft delete — never remove from DB
        batch["is_active"] = False
        _batches[batch_id] = batch
        return BatchResponse(**batch)


batch_service = BatchService()