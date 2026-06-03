# """
# routers/batch.py

# HTTP layer only. Zero business logic here.
# This file's only jobs:
#   1. Accept and validate the request (Pydantic does this)
#   2. Call the service
#   3. Wrap result in response envelope
#   4. Map exceptions to HTTP status codes

# If you find yourself writing if/else logic here
# that isn't about HTTP — move it to the service.
# """
# from uuid import UUID
# from fastapi import APIRouter, HTTPException, Query     
# from app.schemas.batch import BatchCreate, BatchUpdate
# from app.services.batch_service import batch_service
# from app.core.responses import success, paginated
# from app.core.exceptions import NotFoundException, ConflictException
# router = APIRouter(prefix="/batches", tags=["Batches"])

# @router.post("", status_code=201)
# async def create_batch(data: BatchCreate):
#     try:
#         batch = batch_service.create(data)
#         return success(
#             data=batch.model_dump(),
#             message="Batch created successfully",
#         )
#     except ConflictException as e:
#         raise HTTPException(status_code=409, detail=e.message)

# @router.get("")
# async def list_batches(
#     page: int = Query(1, ge=1, description="Page number"),
#     size: int = Query(20, ge=1, le=100, description="Items per page"),
# ):
#     batches, total = batch_service.get_all(page=page, size=size)
#     return paginated(
#         data=[b.model_dump() for b in batches],
#         total=total,
#         page=page,
#         size=size,
#         message="Batches retrieved successfully",
#     )
# @router.get("/{batch_id}")
# async def get_batch(batch_id: UUID):
#     try:
#         batch = batch_service.get_by_id(batch_id)
#         return success(
#             data=batch.model_dump(),
#             message="Batch retrieved successfully",
#         )
#     except NotFoundException as e:
#         raise HTTPException(status_code=404, detail=e.message)

# @router.put("/{batch_id}")
# async def update_batch(batch_id: UUID, data: BatchUpdate):
#     try:
#         batch = batch_service.update(batch_id, data)
#         return success(
#             data=batch.model_dump(),
#             message="Batch updated successfully",
#         )
#     except NotFoundException as e:
#         raise HTTPException(status_code=404, detail=e.message)


# @router.delete("/{batch_id}")
# async def delete_batch(batch_id: UUID):
#     try:
#         batch = batch_service.delete(batch_id)
#         return success(
#             data=batch.model_dump(),
#             message="Batch deleted successfully",
#         )
#     except NotFoundException as e:
#         raise HTTPException(status_code=404, detail=e.message)

from fastapi import APIRouter,HTTPException,Query,Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.responses import success,paginated
from app.core.exceptions import NotFoundException,ConflictException
from app.schemas.batch import BatchCreate,BatchUpdate,BatchResponse
from app.services.batch_service import BatchServices

router=APIRouter(prefix="/batche",tags=["batches"])

@router.post("/",status_code=200)
async def create(data:BatchCreate,db:AsyncSession=Depends(get_db)):
    try:
        batchservice=BatchServices(db)
        batch=await batchservice.create(data)
        return success(
            data=batch,
            message="batch created succesfully"
        )
    except ConflictException as e:
        raise HTTPException(status_code=404,detail=e.message)
    
@router.get("/{batch_id}")
async def get_by_id(batch_id:int,db:AsyncSession=Depends(get_db)):
    try:
        service=BatchServices(db)
        batch=await service.get_by_id(batch_id)
        return success(
            data=batch,
            message="batch retriiveed successfuly"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)
    
@router.get("/",status_code=200)    
async def batch_list(
    page:int=Query(1,ge=1,le=10,description="number od pages"),
    size:int=Query(10,ge=1,le=50,description="items per page"),
    db:AsyncSession=Depends(get_db)):
    service=BatchServices(db)
    batch,total=await service.batch_list(page=page,size=size)
    return paginated(
        data=[b.model_dump() for b in batch],
        total=total,
        size=size,
        page=page,
        message="get all batches"
    )
    
@router.put("/{batch_id}")
async def update(batch_id:int,data:BatchUpdate,db:AsyncSession=Depends(get_db)):
    try:
        services=BatchServices(db)    
        batch=await services.update(batch_id,data)
        return success(
            data=batch.model_dump(),
            message="batch updated succesfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)

@router.get("/name/{name}")
async def get_by_name(name:str,db:AsyncSession=Depends(get_db)):
    try:
        service=BatchServices(db)
        batch= await service.get_by_name(name)
        return success(
            data=[b.model_dump() for b in batch ],
            message="batch retrived succesfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)     
    
@router.delete("/{batch_id}")
async def soft_delete(batch_id:int,db:AsyncSession=Depends(get_db)):
    try:
        services= BatchServices(db)
        batch=await services.soft_delete(batch_id)
        return success(
            data=batch,
            message="batch deactivate successfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)