from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select   
from app.schemas.trainer_profile import TrainerProfileCreate, TrainerProfileResponse, TrainerProfileUpdate
from app.models.trainer_profile import TrainerProfile
from fastapi import HTTPException

class TrainerProfileRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: TrainerProfileCreate) -> TrainerProfile:
        trainer_profile = TrainerProfile(**data.model_dump())
        self.db.add(trainer_profile)
        await self.db.flush()
        await self.db.refresh(trainer_profile)
        return trainer_profile
    
    async def get_by_id(self, trainer_id: int) -> TrainerProfile | None:
        result = await self.db.execute(
            select(TrainerProfile).where(TrainerProfile.trainer_id == trainer_id, TrainerProfile.is_active == True)
        )
        return result.scalar_one_or_none()
    
    async def soft_delete(self, trainer_id: int) -> bool:
        result = await self.db.execute(
            select(TrainerProfile).where(TrainerProfile.trainer_id == trainer_id)
        )
        trainer_profile = result.scalar_one_or_none()
        if not trainer_profile:
            return False
        trainer_profile.is_active = False
        await self.db.flush()
        return True
    
    async def update(self, trainer_profile: TrainerProfile, data: TrainerProfileUpdate) -> TrainerProfile:
     for key, value in data.model_dump(exclude_unset=True).items():
        setattr(trainer_profile, key, value)
     await self.db.flush()
     await self.db.refresh(trainer_profile)
     return trainer_profile
    
    async def get_all(self, page: int, size: int) -> tuple[list[TrainerProfile], int]:
        result = await self.db.execute(
            select(TrainerProfile).where(TrainerProfile.is_active == True).offset((page-1)*size).limit(size)
        )
        trainer_profiles = result.scalars().all()
        total_result = await self.db.execute(
            select(TrainerProfile).where(TrainerProfile.is_active == True)
        )
        total = len(total_result.scalars().all())
        return trainer_profiles, total