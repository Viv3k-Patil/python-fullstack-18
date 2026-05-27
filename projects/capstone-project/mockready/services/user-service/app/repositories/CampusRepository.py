from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.campus import CampusCreate, CampusUpdate
from app.models.campus import Campus



# campus repository

class CampusRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: CampusCreate) -> Campus:
        # CampusCreate -> type -> pydantic schmema
        # Campus -> type > sqlalchemy model

        # step 1: send data to db
        # data-> model, schema -> model and then send it to db
        # 1. model_dump -> pydantic object-> python dict
        # 2. dict unpack
        campus = Campus(**data.model_dump())
        self.db.add(campus)
        await self.db.flush()
        await self.db.refresh(campus)
        return campus
    
    async def get_by_id(self, campus_id: int) -> Campus | None:
        result = await self.db.execute(
            # this is statement
            select(Campus).where(Campus.campus_id ==campus_id, Campus.is_active == True)
        )
        return result.scalar_one_or_none()
    
    async def get_by_name(self, name: str) -> Campus | None:
        result = await self.db.execute(select(Campus).where(Campus.name.ilike(name)))
        return result.scalar_one_or_none()
    
    async def soft_delete(self, campus:Campus) -> bool:
        campus.is_active = False
        await self.db.flush()
        return not campus.is_active
    
    async def update(self, campus: Campus: data: CampusUpdate) -> Campus:
        for key, value in data.model_dump().items():
            # campus[key] = value
            setattr(campus, key, value)
        await self.db.flush()
        await self.db.refresh(campus)
        return campus
        
