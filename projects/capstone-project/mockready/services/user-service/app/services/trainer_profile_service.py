"""
services/trainer_profile_service.py

All business logic lives here. NEVER in the router.

The router calls this. This calls the repository (Phase 2).
When we switch to Postgres in Phase 2 — only this file
changes. The router stays exactly the same.
That is the entire point of this layer.
"""
from app.schemas.trainer_profile import TrainerProfileCreate, TrainerProfileUpdate, TrainerProfileResponse
from app.repositories.TrainerProfileRepository import TrainerProfileRepository       
from sqlalchemy.ext.asyncio import AsyncSession


class TrainerProfileService:

    def __init__(self, db: AsyncSession):
        self.trainer_profile_repo = TrainerProfileRepository(db)

    async def create(self, data: TrainerProfileCreate) -> TrainerProfileResponse:
        trainer_profile = await self.trainer_profile_repo.create(data)
        return TrainerProfileResponse.model_validate(trainer_profile)

    async def get_by_id(self, trainer_profile_id: int) -> TrainerProfileResponse:
        trainer_profile = await self.trainer_profile_repo.get_by_id(trainer_profile_id)
        return TrainerProfileResponse.model_validate(trainer_profile)

    async def get_all(self, page: int, size: int) -> tuple[list[TrainerProfileResponse], int]:
        trainer_profiles, total = await self.trainer_profile_repo.get_all(page, size)
        return [TrainerProfileResponse.model_validate(tp) for tp in trainer_profiles    ], total
    
    
    async def delete(self, trainer_profile_id: int):
        return await self.trainer_profile_repo.soft_delete(trainer_profile_id)
    
    async def update(self, trainer_profile_id: int, data: TrainerProfileUpdate) -> TrainerProfileResponse:
        trainer_profile = await self.trainer_profile_repo.update(trainer_profile_id, data)
        return TrainerProfileResponse.model_validate(trainer_profile)
    