from uuid import UUID
from fastapi import APIRouter,HTTPException,Query
from app.schemas.batch import BatchCreate,BatchResponse,UpdateBatch
from app.services.batch_services import batch_service
from app.core.exceptions import ConflictException,NotFoundException
from app.core.responses import success,paginated

router=APIRouter(prefix="/batches",tags=["batchs"])

@router.post("/",status_code=202)
async def create_batch(data:BatchCreate):
    try:
        batch= batch_service.create(data)
        return success(
        data=batch.model_dump(),#converts the model object into a dict
        message="Batch created sucssesfully"
    )
    except  ConflictException as e:
        raise HTTPException(status_code=409,detail=e.message) 
    
@router.get("/")
async def list_batches( page:int=Query(1,ge=1,description="page number"),
                  size:int=Query(20,ge=1,lt=100,description="Iteams per page")
             ):
    batches,total=batch_service.get_all(page=page,size=size)
    return paginated(
        data=[b.model_dump() for b in batches],
        total=total,
        page=page,
        size=size,
        message="batch retrived succesfully",
        
    )  
    
@router.get("/{batch_id}")
async def get_batch(batch_id:UUID):
    try:
        batch=batch_service.get_by_id(batch_id)
        return success(
            data=batch.model_dump(),
            message="Batch get successfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)  

@router.put("/{batch_id}")
def update_batch(batch_id:UUID,data:UpdateBatch):
    try:    
        batch=batch_service.update_batch(batch_id,data)
        return success(
            data=batch.model_dump(),
            message="batchh updated sucessfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)    
    
    
@router.delete("/{batch_id}")
async def delete_batch(batch_id:UUID):
    try:
        batch= batch_service.delete_batch_by_id(batch_id)
        return success(
            data=batch.model_dump(),
            message="Batch delete Successfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)    
    
   
