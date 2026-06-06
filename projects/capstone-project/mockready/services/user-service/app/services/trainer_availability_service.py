"""
services/Trainer_Availability_Service.py

All business logic lives here. NEVER in the router.

The router calls this. This calls the repository (Phase 2).
When we switch to Postgres in Phase 2 — only this file
changes. The router stays exactly the same.
That is the entire point of this layer.
"""

from app.schemas.trainer_availability import TrainerAvailabilityCreate, TrainerAvailabilityUpdate, TrainerAvailabilityResponse
from app.repositories.TrainerAvailabilityRepository import TrainerAvailabilityRepository
from sqlalchemy.ext.asyncio import AsyncSession


class TrainerAvailabilityService:
    def __init__(self, db: AsyncSession):
        self.trainer_availability_repo = TrainerAvailabilityRepository(db)
    
    async def create(self, data: TrainerAvailabilityCreate) -> TrainerAvailabilityResponse:
        trainer_availability = await self.trainer_availability_repo.create(data)
        return TrainerAvailabilityResponse.model_validate(trainer_availability)
    
    async def get_by_id(self, trainer_availability_id: int)-> TrainerAvailabilityResponse:
        trainer_availability = await self.trainer_availability_repo.get_by_id(trainer_availability_id)
        return TrainerAvailabilityResponse.model_validate(trainer_availability)
    
    async def get_all(self, page: int, size: int) -> tuple[list[TrainerAvailabilityResponse], int]:
        trainer_availabilities, total = await self.trainer_availability_repo.get_all(page, size)
        return [TrainerAvailabilityResponse.model_validate(t) for t in trainer_availabilities], total

    async def update(self, trainer_availability_id: int, data: TrainerAvailabilityUpdate) -> TrainerAvailabilityResponse:
        trainer_availability = await self.trainer_availability_repo.update(trainer_availability_id, data)
        return TrainerAvailabilityResponse.model_validate(trainer_availability)  
       
    async def delete(self, trainer_availability_id: int):
        return await self.trainer_availability_repo.soft_delete(trainer_availability_id)
    