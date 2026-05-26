from sqlalchemy.ext.asyncio import (
    AsyncSession
)
from app.schemas.campus import CampusCreate
from app.models.campus import Campus

class CampusRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: CampusCreate) -> Campus:
        campus = Campus(**data.model_dump())
        await self.db.add(campus)
        await self.db.flush()
        await self.db.refresh()
        return campus
