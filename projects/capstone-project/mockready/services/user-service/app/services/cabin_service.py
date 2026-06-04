from http.client import HTTPException

from app.schemas.cabin import CabinCreate, CabinResponse, CabinUpdate
from app.repositories.CabinRepository import CabinRepository
from sqlalchemy.ext.asyncio import AsyncSession

class CabinService:

    def __init__(self, db : AsyncSession):
       self.cabin_repo = CabinRepository(db)

    async def create(self,data: CabinCreate)->CabinResponse:
        cabin = await self.cabin_repo.create(data)
        return CabinResponse.model_validate(cabin)
    
    async def get_by_id(self,cabin_id: int)->CabinResponse:
        cabin = await self.cabin_repo.get_by_id(cabin_id)
        return CabinResponse.model_validate(cabin)
    
    
    
    async def get_all(self,page:int ,size:int)->tuple[list[CabinResponse],int]:
        cabins,total = await self.cabin_repo.get_all(page,size)
        return [CabinResponse.model_validate(c) for c in cabins],total
    
    async def update(self, cabin_id: int, data: CabinUpdate) -> Cabin:
     cabin = await self.cabin_repo.get_by_id(cabin_id)  # fetch here
     if not cabin:
        raise HTTPException(status_code=404)
     return await self.cabin_repo.update(cabin, data)


    async def delete(self,cabin_id: int):
        return await self.cabin_repo.soft_delete(cabin_id)