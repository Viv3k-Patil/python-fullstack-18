"""
services/Trainer_Campus_Service.py

All business logic lives here. NEVER in the router.

The router calls this. This calls the repository (Phase 2).
When we switch to Postgres in Phase 2 — only this file
changes. The router stays exactly the same.
That is the entire point of this layer.
"""

from http.client import HTTPException

from app.schemas.trainer_campus import TrainerCampusCreate, TrainerCampusResponse
from app.repositories.TrainerCampusRepository import TrainerCampusRepository    
from sqlalchemy.ext.asyncio import AsyncSession

class TrainerCampusService:

    def __init__(self, db: AsyncSession):
        self.repo = TrainerCampusRepository(db)

    async def create(self, data: TrainerCampusCreate) -> TrainerCampusResponse:
        trainer_campus = await self.repo.create(data)
        return TrainerCampusResponse.model_validate(trainer_campus)
    
    async def get_all(self, page: int, size: int) -> tuple[list[TrainerCampusResponse], int]:
        trainer_campuses, total = await self.repo.get_all(page, size)
        return [TrainerCampusResponse.model_validate(tc) for tc in trainer_campuses], total
    
    async def get_by_id(self, trainer_campus_id: int) -> TrainerCampusResponse:
        trainer_campus = await self.repo.get_by_id(trainer_campus_id)
        return TrainerCampusResponse.model_validate(trainer_campus)
    
    async def update(self, trainer_campus_id: int, data: TrainerCampusCreate) -> TrainerCampusResponse:
     trainer_campus = await self.repo.get_by_id(trainer_campus_id)  # fetch first
     if not trainer_campus:
        raise HTTPException(status_code=404, detail="Trainer campus not found")
     trainer_campus = await self.repo.update(trainer_campus, data)  # pass object
     return TrainerCampusResponse.model_validate(trainer_campus)

    async def delete(self, trainer_campus_id: int) -> None:
        await self.repo.soft_delete(trainer_campus_id) 
