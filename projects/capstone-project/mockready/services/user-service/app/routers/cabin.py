from fastapi import APIRouter,HTTPException,Query
from uuid import UUID

from app.core.responses import success,paginated
from app.schemas.cabin import CabinResponse,CreateCabin,UpdateCabin
from app.core.exceptions import NotFoundException,ConflictException
from app.services.cabin_service import cabin_services

router=APIRouter(prefix="/cabins",tags=["cabins"])

@router.post("/",status_code=201)
async def create_cabin(data:CreateCabin):
    try:
        cabin=cabin_services.create(data)
        return success(
            data=cabin.model_dump(),
            message="cabin created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=404,detail=e.message) 
    
@router.get("/")
async def cabin_list(
        page:int=Query(1 ,ge=1,description="page number"),
        size:int=Query(20,ge=1,lt=100,description="items per page")
    ):
        cabins,total=cabin_services.get_all(page=page,size=size)
        return paginated(
            data=[c.model_dump() for c in cabins],
            total=total,
            page=page,
            size=size,
            message="get all cabins Succesfully",
        )
        
@router.get("/{cabin_id}") 
async def get_cabins(cabin_id:UUID):
    try:    
        cabin=cabin_services.get_by_id(cabin_id)
        return success(
            data=cabin.model_dump(),
            message="cabin retrived succesfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)

@router.put("/{cabin_id}")
async def update_cabin(cabin_id:UUID,data:UpdateCabin):
    try:    
        cabin=cabin_services.update(cabin_id,data)
        return success(
            data=cabin.model_dump(),
            message="cabin updated successfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)    
    
@router.delete("/{cabin_id}")
async def delete_cabin(cabin_id: UUID):
    try:
        cabin = cabin_services.delete(cabin_id)

        return success(
            data=cabin.model_dump(),
            message="Cabin deleted successfully",
        )

    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)   