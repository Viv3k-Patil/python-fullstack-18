

from fastapi import APIRouter,HTTPException,Query,Depends
from app.schemas.cabin import CabinCreate,CabinUpdate
from app.services.cabin_service import CabinService
from app.core.responses import success,paginated
from app.core.exceptions import NotFoundException,ConflictException
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix="/cabins",tags=["Cabins"])

@router.post("",status_code=201)
async def create_cabin(data: CabinCreate,db: AsyncSession = Depends(get_db)):
    try:
        cabin = await CabinService(db).create(data)
        return success(
            data=cabin,
            message="Cabin created successfully",
        )
    except ConflictException as e:
        raise HTTPException(status_code=409,detail=e.message)  
    question = "What is the purpose of the `ConflictException` in the `create_cabin` function?"
    answer = "The `ConflictException` is used to handle cases where there is a conflict during the creation of a cabin, such as when a cabin with the same name already exists. If this exception is raised, it will return a 409 HTTP status code with the appropriate error message."
@router.get("")
async def list_cabins(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: AsyncSession = Depends(get_db)
):
    cabins, total = await CabinService(db).get_all(page=page, size=size)
    return paginated(
        data=[c.model_dump() for c in cabins],
        total=total,
        page=page,
        size=size,
        message="Cabins retrieved successfully",
    )

@router.get("/{cabin_id}")
async def get_cabin(cabin_id: int,db : AsyncSession = Depends(get_db)):
    try:
        cabin = await CabinService(db).get_by_id(cabin_id)
        return success(
            data=cabin.model_dump(),
            message="Cabin retrieved successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

@router.put("/{cabin_id}")
async def update_cabin(cabin_id: int, data: CabinUpdate,db : AsyncSession = Depends(get_db)):
    try:
        cabin = await CabinService(db).update(cabin_id, data)
        return success(
            data=cabin.model_dump(),
            message="Cabin updated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

@router.delete("/{cabin_id}")
async def delete_cabin(cabin_id: int,db : AsyncSession = Depends(get_db)):
    try:
        is_deleted =  await CabinService(db).delete(cabin_id)
        return success(
            data=is_deleted,
            message="Cabin deleted successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
     
