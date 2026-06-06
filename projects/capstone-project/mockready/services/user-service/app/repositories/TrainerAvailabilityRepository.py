from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.trainer_availability import TrainerAvailabilityCreate, TrainerAvailabilityUpdate
from app.models.trainer_availability import TrainerAvailability


# trainer availability repository

class TrainerAvailabilityRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: TrainerAvailabilityCreate) -> TrainerAvailability:
        trainer_availability = TrainerAvailability(**data.model_dump())
        self.db.add(trainer_availability)
        await self.db.flush()
        await self.db.refresh(trainer_availability)
        return trainer_availability
    
    async def get_by_id(self, trainer_availability_id: int) -> TrainerAvailability | None:
        result = await self.db.execute(
            select(TrainerAvailability).where(TrainerAvailability.trainer_availability_id == trainer_availability_id, TrainerAvailability.is_active == True)
        )
        return result.scalar_one_or_none()
    
    async def soft_delete(self, trainer_availability_id: int) -> bool:
        result = await self.db.execute(
            select(TrainerAvailability).where(TrainerAvailability.trainer_availability_id == trainer_availability_id)
        )
        trainer_availability = result.scalar_one_or_none()
        if not trainer_availability:
            return False
        trainer_availability.is_active = False
        await self.db.flush()
        return True
    
    async def update(self, trainer_availability: TrainerAvailability, data: TrainerAvailabilityUpdate) -> TrainerAvailability:
        for key, value in data.model_dump().items():
            setattr(trainer_availability, key, value)
        await self.db.flush()
        await self.db.refresh(trainer_availability)
        return trainer_availability
        
    async def get_all(self, page: int, size: int) -> tuple[list[TrainerAvailability], int]:
        result = await self.db.execute(
            select(TrainerAvailability).where(TrainerAvailability.is_active == True).offset((page-1)*size).limit(size)
        )
        counts = result.scalars().all()
        total_result = await self.db.execute(
            select(TrainerAvailability).where(TrainerAvailability.is_active == True)
        )
        total = len(total_result.scalars().all())
        return counts, total
