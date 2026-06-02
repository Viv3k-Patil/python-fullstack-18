from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.trainer_availability import (
    TrainerAvailabilityCreate,
    TrainerAvailabilityUpdate
)
from app.models.trainer_availability import TrainerAvailability


class TrainerAvailabilityRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: TrainerAvailabilityCreate) -> TrainerAvailability:
        availability = TrainerAvailability(**data.model_dump())
        self.db.add(availability)
        await self.db.flush()
        await self.db.refresh(availability)
        return availability

    async def get_by_id(self, availability_id: int) -> TrainerAvailability | None:
        result = await self.db.execute(
            select(TrainerAvailability).where(
                TrainerAvailability.id == availability_id
            )
        )
        return result.scalar_one_or_none()

    async def get_by_trainer(self, trainer_id: int) -> list[TrainerAvailability]:
        result = await self.db.execute(
            select(TrainerAvailability).where(
                TrainerAvailability.trainer_id == trainer_id
            )
        )
        return result.scalars().all()

    async def get_all(self, page: int, size: int) -> tuple[list[TrainerAvailability], int]:
        result = await self.db.execute(
            select(TrainerAvailability)
            .offset((page - 1) * size)
            .limit(size)
        )
        availabilities = result.scalars().all()

        count_result = await self.db.execute(
            select(TrainerAvailability)
        )
        total = len(count_result.scalars().all())

        return availabilities, total

    async def update(
        self,
        availability: TrainerAvailability,
        data: TrainerAvailabilityUpdate
    ) -> TrainerAvailability:
        for key, value in data.model_dump().items():
            if value is not None:
                setattr(availability, key, value)

        await self.db.flush()
        await self.db.refresh(availability)
        return availability

    async def delete(self, availability_id: int) -> bool:
        result = await self.db.execute(
            select(TrainerAvailability).where(
                TrainerAvailability.id == availability_id
            )
        )
        availability = result.scalar_one_or_none()

        if not availability:
            return False

        await self.db.delete(availability)
        await self.db.flush()
        return True