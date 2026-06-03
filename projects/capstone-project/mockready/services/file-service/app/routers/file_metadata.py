from fastapi import APIRouter, HTTPException, Query, UploadFile, File, Form, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.responses import success, paginated
from app.schemas.file_metadata import FileCreate, FileResponse, FileUpdate
from app.services.file_metatdata_service import FileMetadataService
from app.core.exception import (
    ConflictException,
    NotFoundException,
    FileToLargeException,
    InvalidFileTypeException
)

router = APIRouter(
    prefix="/file_metadata",
    tags=["file_metadata"]
)

@router.post("/", status_code=201)
async def create_metadata(
    student_id: int = Form(...),
    student_name: str = Form(..., description="add name here"),
    fileupload: UploadFile = File(..., description="upload file here"),
    db: AsyncSession = Depends(get_db)
):
    try:
        data = FileCreate(
            student_id=student_id,
            student_name=student_name,
            # ✅ no file here
        )
        service = FileMetadataService(db)
        file = await service.create(data, fileupload)   # ✅ pass separately

        return success(
            data=file.model_dump(),
            message="File metadata created successfully"
        )
    except ConflictException as e:
        raise HTTPException(status_code=409, detail=e.message)
    except FileToLargeException as e:
        raise HTTPException(status_code=413, detail=e.message)
    except InvalidFileTypeException as e:
        raise HTTPException(status_code=415, detail=e.message)


@router.get("/")
async def list_file(                                                     # ✅ async added
    page: int = Query(2, ge=1, description="page number"),
    size: int = Query(20, ge=1, le=100, description="Items per page"),   # ✅ le= not ls=
    db: AsyncSession = Depends(get_db)                               # ✅ inject db session
):
    service = FileMetadataService(db)                                   # ✅ instantiate
    file, total = await service.file_list(page=page, size=size)          # ✅ await + instance call
    return paginated(
        data=[f.model_dump() for f in file],
        total=total,
        page=page,
        size=size,
        message="file_metadata retrieved successfully",
    )


@router.get("/{id}")
async def get_id(                                                        # ✅ async added
    id: int,
    db: AsyncSession = Depends(get_db)                                   # ✅ inject db session
):
    try:
        service = FileMetadataService(db)                               # ✅ instantiate
        file = await service.get_by_id(id)                              # ✅ await + instance call
        return success(
            data=file.model_dump(),
            message="file_metadata retrieved successfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.get("/name/{student_name}")
async def get_by_name(
           student_name:str,
           db:AsyncSession =Depends(get_db)     
        ):
    try:
        service=FileMetadataService(db)
        file=await service.get_by_name(student_name)
        return success(
            data=[f.model_dump() for f in file],
            message="student name is retrived succesfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404,detail=e.message)    
        


@router.put("/{id}")
async def update_id(                                                     # ✅ async added
    id: int,
    data: FileUpdate,
    db: AsyncSession = Depends(get_db)                                   # ✅ inject db session
):
    try:
        service = FileMetadataService(db)                               # ✅ instantiate
        file = await service.update(id, data)                            # ✅ await + instance call
        return success(
            data=file.model_dump(),
            message="file updated successfully"
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.delete("/{id}")
async def delete_file(
    id: int,
    db: AsyncSession = Depends(get_db)                                   #  inject db session
):
    try:
        service = FileMetadataService(db)                               # instantiate
        file = await service.soft_delete(id)                             #  await + instance call
        return success(
            data=file,
            message="file deactivated successfully",
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)