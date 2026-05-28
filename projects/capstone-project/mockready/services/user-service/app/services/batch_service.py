from app.repositories.BatchRepository import BatchRepository
from app.schemas.batch import BatchCreate,  BatchResponse
from sqlalchemy.ext.asyncio import AsyncSession

class BatchService: 
    def __init__(self,db:AsyncSession):
        self.batch_repo = BatchRepository(db)

    async def create(self, data: BatchCreate) -> BatchResponse:
        batch = await self.batch_repo.create(data)
        return BatchResponse.model_validate(batch)
        
    async def get_all(self, page: int, size: int) -> tuple[list[BatchResponse], int]:
        batches, total = await self.batch_repo.get_all(page,size)
        return[BatchResponse.model_validate(b) for b in batches],total
    
    async def get_by_id(self, batch_id: int) -> BatchResponse:
        batch= await self.batch_repo.get_by_id(batch_id)
        return BatchResponse.model_validate(batch)     

    async def delete(self, batch_id: int) :
        return await self.batch_repo.soft_delete(batch_id)
        
    

