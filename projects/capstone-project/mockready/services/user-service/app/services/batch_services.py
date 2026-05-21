from uuid import UUID,uuid4
from datetime import datetime,timezone

from app.schemas.batch import BatchCreate,BatchResponse,UpdateBatch
from app.core.exceptions import ConflictException,NotFoundException


_batch:dict[UUID,dict]={}



class BatchServices():
    
    def create(self,data:BatchCreate)->BatchResponse:
        #bussiness logic->no duplicate batch names
       
        for b in _batch.values():
            if b["name"].lower()==data.name.lower():
                raise ConflictException(f"batch {data.name} already exist")
                
        batch={
           "id":uuid4(),
           "name":data.name,
           "campus_id":data.campus_id,
           "course":data.course,
           "start_date":datetime.now(timezone.utc),
           "end_date":datetime.now(timezone.utc),
           "is_active":True
        }        
        
        _batch[batch["id"]]=batch
        return BatchResponse(**batch)
    
    def get_all(self,page:int,size:int)->tuple[list[BatchResponse],int]:
       active=[b for b in _batch.values() if b["is_active"]]
       total=len(active)
       start=(page-1)*size
       chunks=active[start:start+size] 
       return [BatchResponse(**b) for b in chunks],total
   
    def get_by_id(self,batch_id:UUID):
        batch=_batch.get(batch_id)
        if not batch or not batch["is_active"]:
            raise NotFoundException(f"batch {batch_id} not found")
        return BatchResponse(**batch)
    
    def update_batch(self,batch_id:UUID,data:UpdateBatch):
        batch= _batch.get(batch_id)
        if not batch or not batch["is_active"]:
           raise NotFoundException(f"batch {batch_id} not found")
          
        # only update fields the client actually sent
        updates=data.model_dump(exclude_none=True)
        batch.update(updates)
        _batch["batch_id"]=batch
        
        return BatchResponse(**batch)
    
    def delete_batch_by_id(self,batch_id:UUID)->BatchResponse:
       batch= _batch.get(batch_id)
       if not batch or not batch["is_active"]:
           raise NotFoundException(f"batch {batch_id} not found")
       
        # always soft delete — never remove from DB
       batch["is_active"]=False
       return BatchResponse(**batch)
   
batch_service =BatchServices()