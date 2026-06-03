# from uuid import UUID, uuid4
# from datetime import datetime, timezone

# from app.schemas.batch import BatchCreate, BatchUpdate, BatchResponse
# from app.core.exceptions import NotFoundException, ConflictException


# batches: dict[UUID, dict] = {}  

# class BatchService: 
#     def create(self, data: BatchCreate) -> BatchResponse:
#         batch = {
#             "id": uuid4(),
#             "name": data.name,
#             "course":data.course,
#             "campus_id": data.campus_id,
#             "is_active": True,
#             "created_at": datetime.now(timezone.utc),
#             "start_time":datetime.now(timezone.utc),
#             "end_time":datetime.now(timezone.utc)
#         }
#         batches[batch["id"]] = batch
#         return BatchResponse(**batch)

#     def get_all(self, page: int, size: int) -> tuple[list[BatchResponse], int]:
#         active = [b for b in batches.values() if b["is_active"]]
#         total = len(active)
#         start = (page - 1) * size
#         chunk = active[start: start + size]
#         return [BatchResponse(**b) for b in chunk], total

#     def get_by_id(self, batch_id: UUID) -> BatchResponse:
#         batch = batches.get(batch_id)
#         if not batch or not batch["is_active"]:
#             raise NotFoundException(f"Batch {batch_id} not found")
#         return BatchResponse(**batch)

#     def update(self, batch_id: UUID, data: BatchUpdate) -> BatchResponse:
#         batch = batches.get(batch_id)
#         if not batch or not batch["is_active"]:
#             raise NotFoundException(f"Batch {batch_id} not found")

#         updates = data.model_dump(exclude_none=True)
#         batch.update(updates)
#         batches[batch_id] = batch
#         return BatchResponse(**batch)

#     def delete(self, batch_id: UUID) -> BatchResponse:
#         batch = batches.get(batch_id)
#         if not batch or not batch["is_active"]:
#             raise NotFoundException(f"Batch {batch_id} not found")

#         batch["is_active"] = False
#         batches[batch_id] = batch
#         return BatchResponse(**batch)
    

# batch_service = BatchService()  

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import NotFoundException,ConflictException
from app.repositories.BatchRepository import BatchRepository
from app.schemas.batch import BatchCreate,BatchResponse,BatchUpdate

class BatchServices:
    def __init__(self,db:AsyncSession):
        self.batch_repo=BatchRepository(db)
        
    async def create(self,data:BatchCreate)->BatchResponse:    
        batch=await self.batch_repo.create(data)
        return BatchResponse.model_validate(batch)
    
    async def get_by_id(self,batch_id:int)->BatchResponse:
       batch= await self.batch_repo.get_by_id(batch_id)
       
       if batch is None:
           return NotFoundException(message=f"batch {batch_id} is not found")
       return BatchResponse.model_validate(batch)
   
   
    async def get_by_name(self,name:str)->list[BatchResponse]:
        batch=await self.batch_repo.get_by_name(name)
        if batch is None:
            raise NotFoundException(f"name {name} is not found")
        return [BatchResponse.model_validate(b) for b in batch] 
    
    async def batch_list(self,page:int,size:int)->tuple[list[BatchResponse],int]:
        batch,total= await self.batch_repo.batch_list(page,size)
        return [BatchResponse.model_validate(b)for b in batch],total
    
    async def update(self,batch_id:int,data:BatchUpdate)->BatchResponse:
        batch=await self.batch_repo.update(batch_id,data)
        return BatchResponse.model_validate(batch)
    
    async def soft_delete(self,batch_id:int)->None:
        return await self.batch_repo.soft_delete(batch_id)