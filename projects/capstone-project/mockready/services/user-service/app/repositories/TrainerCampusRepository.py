from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.trainer_campus import TrainerCampusCreate, TrainerCampusUpdate
from app.models.trainer_campus import TrainerCampus 


# trainer campus repository
class TrainerCampusRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: TrainerCampusCreate) -> TrainerCampus:
        trainer_campus = TrainerCampus(**data.model_dump())
        self.db.add(trainer_campus)
        await self.db.flush()
        await self.db.refresh(trainer_campus)
        return trainer_campus
    
    async def get_by_id(self, trainer_campus_id: int) -> TrainerCampus | None:
        result = await self.db.execute(
            select(TrainerCampus).where(TrainerCampus.trainer_campus_id == trainer_campus_id, TrainerCampus.is_active == True)
        )
        return result.scalar_one_or_none()
    
    async def soft_delete(self, trainer_campus_id: int) -> bool:
        result = await self.db.execute(
            select(TrainerCampus).where(TrainerCampus.trainer_campus_id == trainer_campus_id)
        )
        trainer_campus = result.scalar_one_or_none()
        if not trainer_campus:
            return False
        trainer_campus.is_active = False
        await self.db.flush()
        return True
    
    async def update(self, trainer_campus: TrainerCampus, data: TrainerCampusUpdate) -> TrainerCampus:
        for key, value in data.model_dump().items():
            setattr(trainer_campus, key, value)
        await self.db.flush()
        await self.db.refresh(trainer_campus)
        return trainer_campus
        
    async def get_all(self, page: int, size: int) -> tuple[list[TrainerCampus], int]:
        result = await self.db.execute(
            select(TrainerCampus).where(TrainerCampus.is_active == True).offset((page-1)*size).limit(size)
        )
        trainer_campuses = result.scalars().all()
        total_result = await self.db.execute(
            select(TrainerCampus).where(TrainerCampus.is_active == True)
        )
        total = len(total_result.scalars().all())
        return trainer_campuses, total