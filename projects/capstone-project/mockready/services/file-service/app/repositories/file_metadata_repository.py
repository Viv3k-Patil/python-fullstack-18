from fastapi import UploadFile,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date,timezone

from sqlalchemy import select,func
from app.schemas.file_metadata import FileCreate,FileUpdate
from app.models.file_metadata import FileMetadata


class MetaDataRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

# repository
    async def create(
        self,
        data: FileCreate,        # ✅ data first
        fileupload: UploadFile,  # ✅ file second
    ) -> FileMetadata:
        content = await fileupload.read()
        # rest stays the same...

        # Create stored path
        stored_path = f"memory/{fileupload.filename}"

        # Create DB object
     
        filemetadata = FileMetadata(
            student_id=data.student_id,
            student_name=data.student_name,
            stored_path=stored_path,
            file_type=fileupload.content_type,
            size_bytes=len(content),
            uploaded_at=date.today(),
            is_active=True

        )

        self.db.add(filemetadata)

        await self.db.flush()
        await self.db.refresh(filemetadata)

        return filemetadata
    
    async def get_by_id(self,id:int)->FileMetadata|None:
        result=await self.db.execute(
            select(FileMetadata).where(FileMetadata.id==id)
        )
        
        return result.scalar_one_or_none()
    
    async def get_by_name(self,student_name:str)->list[FileMetadata]:
        result=await self.db.execute(
            select(FileMetadata).where(FileMetadata.student_name==student_name)
        )
        return result.scalars().all()

    
    async def soft_delete(self,id:int):
        result=await self.db.execute(
            select(FileMetadata).where(FileMetadata.id==id)
        )
        
        file=result.scalar_one_or_none()

        if file is None:
            raise HTTPException(
                status_code=404,
                detail="file not found"
            )
        
        await self.db.delete(file)
        # await self.db.flush()
        # await self.db.commit()
        
    
      
    async def update(self,id:int,data:FileUpdate)->FileMetadata:
        result= await self.db.execute(
            select(FileMetadata).where(FileMetadata.id==id)
        )
        file=result.scalar_one_or_none()
        
        
        for key,val in data.model_dump(exclude_unset=True,exclude={"id"}).items():
            setattr(file,key,val)
            
        await self.db.flush()
        await self.db.refresh(file)
        return file
    
    async def file_list(self,page=int,size=int)->tuple[list[FileMetadata],int]:
        result=await self.db.execute(
            select(FileMetadata).where(FileMetadata.is_active==True).offset((page-1)*size).limit(size)
            )
        file= result.scalars().all()
        
        total_files=await self.db.execute(
            select(func.count()).select_from(FileMetadata).where(FileMetadata.is_active==True)
        )
        total=total_files.scalar()
        
        return file,total

      