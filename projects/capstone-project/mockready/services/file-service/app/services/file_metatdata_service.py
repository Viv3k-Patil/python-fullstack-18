
# from datetime import datetime, timezone
# from fastapi import UploadFile

# from app.utils.utils import upload_file
# from app.schemas.file_metadata import ( FileResponse, FileUpdate,)
# from app.core.exception import  ConflictException,NotFoundException


# _metadata: dict[int, dict] = {}


# class FileMetaDataServices:

#     async def create(self,
#                student_id:int,
#                student_name:str,
#                uploaded_file:UploadFile
#                ) -> FileResponse:
#         # Check duplicate name
#         for m in _metadata.values():
#             if m["student_name"].lower() == student_name.lower():
#                 raise ConflictException(
#                     f"student '{student_name}' already exists"
#                 )
                
#         file_info=upload_file(uploaded_file)    
        
        
#         new_id = len(_metadata) + 1  
          

#         file_data = {
#             "id": new_id,
#             "student_id": student_id,
#             "student_name": student_name,
#             "original_name": file_info["original_name"],
#             "stored_path": file_info["stored_path"],
#             "file_type": file_info["file_type"],
#             "size_bytes": file_info["size_bytes"],
#             "uploaded_at": datetime.now(timezone.utc),
#             "is_active": True
#         }

#         _metadata[file_data["id"]] = file_data
     
#         return FileResponse(**file_data)

#     def file_list(self,page:int,size:int)->tuple[list[FileResponse],int]:
#         active=[m for m in _metadata.values() if m["is_active"]]
#         total=len(active)
#         start=(page-1)*size
#         chunks=active[start:start+size]
#         return [FileResponse(**m) for m in chunks],total

#     def get_by_id(self,file_id:int):
#        file= _metadata.get(file_id)
#        if not file or not file["is_active"]:
#            raise NotFoundException(f"file {file_id} is not found")
#        return FileResponse(**file)
   
#     def update(self,file_id:int,data:FileUpdate):
#        file =_metadata.get(file_id)
#        if not file or not file["is_active"]:
#            raise NotFoundException(f"file id {file_id} is not found")
       
#        updates=data.model_dump(exclude_none=True)
#        file.update(updates)
#        _metadata[file_id]=file
#        return FileResponse(**file)
   
#     def delete(self,file_id:int):
#        file=_metadata.get(file_id)
#        if not file or not file["is_active"]:
#            raise NotFoundException(f"file id {file_id} is not found")
        
#        file["is_active"]=False
#        _metadata[id]=file 
#        return FileResponse(**file)
       

# filemetadata_services = FileMetaDataServices()


from fastapi import UploadFile
from app.schemas.file_metadata import FileCreate, FileResponse,FileUpdate
from app.repositories.file_metadata_repository import MetaDataRepository
from sqlalchemy.ext.asyncio import AsyncSession

class FileMetadataService:

    def __init__(self, db: AsyncSession):
        self.async_repo = MetaDataRepository(db)

    async def create(self, data: FileCreate, uploaded_file: UploadFile) -> FileResponse:
        file = await self.async_repo.create(data, uploaded_file)  # ✅ pass both
        return FileResponse.model_validate(file)
    
    async def get_by_id(self,id:int)->FileResponse:
        file=await self.async_repo.get_by_id(id)
        return FileResponse.model_validate(file)      
    
    async def get_by_name(self,student_name:str)->list[FileResponse]:
       file= await self.async_repo.get_by_name(student_name)
       return [FileResponse.model_validate(f)for f in file]
   
    async def soft_delete(self,id:int)->None:
        return await self.async_repo.soft_delete(id)
    
    async def update(self,id:int,data:FileUpdate)->FileResponse:
       file= await self.async_repo.update(id,data)
       return FileResponse.model_validate(file)
         
    
    async def file_list(self,page:int,size:int)->tuple[list[FileResponse],int]:
        file,total=await self.async_repo.file_list(page,size)
        return [FileResponse.model_validate(f) for f in file],total