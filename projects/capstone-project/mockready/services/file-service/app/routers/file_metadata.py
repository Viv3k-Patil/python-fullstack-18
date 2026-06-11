from fastapi import APIRouter, HTTPException,Query
from uuid import UUID
from app.core.responses import success,paginated
from app.schemas.file_metadata import FileCreate, FileResponse,FileUpdate
from app.services.file_metadata_service import filemetadata_services
from app.core.exception import ConflictException,NotFoundException

router = APIRouter(
    prefix="/file_metadata",
    tags=["file_metadata"]
)


@router.post("/", status_code=201)
async def create_metadata(data: FileCreate):
    try:
        file = filemetadata_services.create(data)

        return success(
            data=file.model_dump(),
            message="File metadata created successfully"
        )

    except ConflictException as e:
        raise HTTPException(
            status_code=409,
            detail=e.message
        )
@router.get("/")
def list_file(
            page:int=Query(1,ge=1,description="page number"),
            size:int=Query(20,ge=1,ls=100,description="Items per page")
              ) : 
                
                file,total=filemetadata_services.file_list(page=page,size=size,)
                return paginated(
                    data=[f.model_dump() for f in file],
                    total=total,
                    page=page,
                    size=size,
                    message="file_metadata retrived succesfully",
                )
  
@router.get("/{file_id}")
def get_id(file_id:UUID):
    try:
        file=filemetadata_services.get_by_id(file_id)               
        return success(
            data=file.model_dump(),
            message="file_metadata retrived succesfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message) 
    
@router.put("/{file_id}")   
def update_id(file_id:UUID,data:FileUpdate):
    try:
        file=filemetadata_services.update(file_id,data)    
        return success(
            data=file.model_dump(),
            message="file updated succesfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)
    
@router.delete("/{file_id}")
async def delete_file(file_id: UUID):
    try:
        file = filemetadata_services.delete(file_id)
        return success(
            data=file.model_dump(),
            message="file deactivated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)        