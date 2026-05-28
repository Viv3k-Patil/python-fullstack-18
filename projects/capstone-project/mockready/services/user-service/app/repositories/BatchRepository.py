from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.batch import BatchCreate, BatchUpdate
from app.models.batch import Batch



class BatchRepository:
    def __init__(self,db:AsyncSession):
        self.db = db
     
    async def create(self, data : BatchCreate) -> Batch:
    
     batch = Batch(**data.model_dump())
     self.db.add(batch)
     await self.db.flush()
     await self.db.refresh(batch)
     return batch
    
    async def  get_by_id(self,batch_id:int)->Batch | None:
       result = await self.db.execute(
          select(Batch).where(Batch.batch_id == batch_id,Batch.is_active == True)
       )
       return result.scalar_one_or_none()
    
    async def  get_by_name(self,name:str)->Batch | None:
       result = await self.db.execute(
          select(Batch).where(Batch.name == name,Batch.is_active == True)
       )
       return result.scalar_one_or_none()
    
    
    async def soft_delete(self, Batch_id: int) -> bool:
        result = await self.db.execute(
            select(Batch).where(Batch.Batch_id == Batch_id)
        )
        batch = result.scalar_one_or_none()
        if not batch:
            return False
        batch.is_active = False
        await self.db.flush()
        return True
    
    async def update(self,batch:Batch, data : BatchUpdate)->Batch:
       for key,value in data.model_dump().items():
          setattr(batch,key,value)
       await self.db.flush()
       await self.db.refresh(batch)
       return batch
    
    async def get_all(self,page: int ,size: int)->tuple[list[Batch],int]:
       result = await self.db.execute(
         select(Batch).where(Batch.is_active == True).offset((page -1 )* size).limit(size)
       )

       batches = result.scalars().all()

       count_result = await self.db.execute(
         select(Batch).where(Batch.is_active == True)
       )

       total = len(count_result.scalars().all())
       return batches, total
    