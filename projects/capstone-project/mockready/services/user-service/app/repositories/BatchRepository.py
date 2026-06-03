from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,func

from app.schemas.batch import BatchCreate,BatchUpdate,BatchResponse
from app.models.batch import Batch

class BatchRepository:
    
    def __init__(self,db:AsyncSession):
        self.db=db
        
    async def create(self,data:BatchCreate)->Batch:
            #BatchCreate->type->pytantic schema
            #Batch->type->sqlAlchemy model
            #step 1: send data to db
            #data->model schema->model,then send to db
            # 1. model_dump -> pydantic object-> python dict
            # 2. dict unpack
            
            batch=Batch(**data.model_dump())
            self.db.add(batch)
            await self.db.flush()
            await self.db.refresh(batch)
            return batch
    
    async def batch_list(self,page:int,size:int)->tuple[list[Batch],int]:
        result=await self.db.execute(
            select(Batch).where(Batch.is_active==True).offset((page-1)*size).limit(size)
        )
        batch=result.scalars().all()

        total_count=await self.db.execute(
            select(func.count()).select_from(Batch).where(Batch.is_active==True)
        )
        total=total_count.scalar()
        
        return batch,total
    
    async def get_by_id(self,batch_id:int)->Batch|None:
        result=await self.db.execute(
            select(Batch).where(Batch.batch_id==batch_id ,Batch.is_active== True)
        )
        
        return result.scalar_one_or_none()
        
    async def get_by_name(self,name:str)->list[Batch]:    
        result=await self.db.execute(
            select(Batch).where(Batch.name==name , Batch.is_active==True)
        )
        
        return result.scalars().all()
    
    async def update(self,batch_id:int,data:BatchUpdate)->Batch:
            result=await self.db.execute(
                select(Batch).where(Batch.batch_id==batch_id)
            )
            file=result.scalar_one_or_none()    

            for key,val in data.model_dump(exclude_unset=True,exclude={"batch_id"}).items():
                
                setattr(file,key,val)
                
            await self.db.flush()
            await self.db.refresh(file)  
            return file
                
    
    async def soft_delete(self,batch_id:int)->bool:
        result=await self.db.execute(
            select(Batch).where(Batch.batch_id==batch_id , Batch.is_active==True)
        )
        batch=result.scalar_one_or_none()
        
        if batch is None:
            raise HTTPException(
                status_code=404,
                detail="batch not found"
            )
            
        await self.db.delete(batch)
        await self.db.refresh(batch)
        await self.db.commit()