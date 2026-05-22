from uuid import UUID, uuid4
from datetime import datetime, timezone

from app.schemas.batch import BatchCreate, BatchUpdate, BatchResponse
from app.core.exceptions import NotFoundException, ConflictException


batches: dict[UUID, dict] = {}  

class BatchService: 
    def create(self, data: BatchCreate) -> BatchResponse:
        batch = {
            "id": uuid4(),
            "name": data.name,
            "course":data.course,
            "campus_id": data.campus_id,
            "is_active": True,
            "created_at": datetime.now(timezone.utc),
            "start_time":datetime.now(timezone.utc),
            "end_time":datetime.now(timezone.utc)
        }
        batches[batch["id"]] = batch
        return BatchResponse(**batch)

    def get_all(self, page: int, size: int) -> tuple[list[BatchResponse], int]:
        active = [b for b in batches.values() if b["is_active"]]
        total = len(active)
        start = (page - 1) * size
        chunk = active[start: start + size]
        return [BatchResponse(**b) for b in chunk], total

    def get_by_id(self, batch_id: UUID) -> BatchResponse:
        batch = batches.get(batch_id)
        if not batch or not batch["is_active"]:
            raise NotFoundException(f"Batch {batch_id} not found")
        return BatchResponse(**batch)

    def update(self, batch_id: UUID, data: BatchUpdate) -> BatchResponse:
        batch = batches.get(batch_id)
        if not batch or not batch["is_active"]:
            raise NotFoundException(f"Batch {batch_id} not found")

        updates = data.model_dump(exclude_none=True)
        batch.update(updates)
        batches[batch_id] = batch
        return BatchResponse(**batch)

    def delete(self, batch_id: UUID) -> BatchResponse:
        batch = batches.get(batch_id)
        if not batch or not batch["is_active"]:
            raise NotFoundException(f"Batch {batch_id} not found")

        batch["is_active"] = False
        batches[batch_id] = batch
        return BatchResponse(**batch)
    

batch_service = BatchService()  