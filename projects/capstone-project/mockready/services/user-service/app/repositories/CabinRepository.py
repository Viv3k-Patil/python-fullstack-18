from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.cabin import CabinCreate,CabinUpdate
from app.models.cabin import Cabin



class CabinRepository:
    def __init__(self,db:AsyncSession):
        self.db = db

    async def create(self,data:CabinCreate)->Cabin:
        cabin = Cabin(**data.model_dump())
        self.db.add(cabin)
        await self.db.flush()
        await self.db.refresh(cabin)
        return cabin    
    
    async def get_by_id(self,cabin_id:int)->Cabin | None:
        result = await self.db.execute(
            select(Cabin).where(Cabin.cabin_id == cabin_id,Cabin.is_active==True)
        )
        return result.scalar_one_or_none()
    
    async def get_all(self,page:int , size : int)->tuple[list[Cabin],int]:
        result = await self.db.execute(
            select(Cabin).where(Cabin.is_active==True).offset((page-1)*size).limit(size)
        )
        cabins = result.scalars().all()

        count_result = await self.db.execute(
            select(Cabin).where(Cabin.is_active == True)
        )
        total = len(count_result.scalars().all())
        return cabins,total
    
    async def update(self,cabin:Cabin,data:CabinUpdate)->Cabin:
        for key,value in data.model_dump().items():
            setattr(cabin,key,value)
        await self.db.flush()
        await self.db.refresh(cabin)
        return cabin
    
    async def soft_delete(self, cabin_id : int) -> bool:
        result = await self.db.execute(
            select(Cabin).where(Cabin.cabin_id == cabin_id)

        )
        cabin = result.scalar_one_or_none()
        if not cabin:
            return False
        cabin.is_active = False
        await self.db.flush()
        return True