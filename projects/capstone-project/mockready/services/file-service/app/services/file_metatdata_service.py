from uuid import UUID, uuid4
from datetime import datetime, timezone

from app.schemas.file_metadata import (FileCreate, FileResponse, FileUpdate,)
from app.core.exception import  ConflictException,NotFoundException


_metadata: dict[UUID, dict] = {}


class FileMetaDataServices:

    def create(self, data: FileCreate) -> FileResponse:
        # Check duplicate file name
        for m in _metadata.values():
            if m["original_name"].lower() == data.original_name.lower():
                raise ConflictException(
                    f"File name '{data.original_name}' already exists"
                )

        file = {
            "id": uuid4(),
            "student_id": data.student_id,
            "original_name": data.original_name,
            "stored_path": data.stored_path,
            "file_type": data.file_type,
            "size": data.size,
            "uploaded_at": datetime.now(timezone.utc),
            "is_active":True
        }

        _metadata[file["id"]] = file
     
        return FileResponse(**file)

    def file_list(self,page:int,size:int)->tuple[list[FileResponse],int]:
        active=[m for m in _metadata.values() if m["is_active"]]
        total=len(active)
        start=(page-1)*size
        chunks=active[start:start+size]
        return [FileResponse(**m) for m in chunks],total

    def get_by_id(self,file_id:UUID):
       file= _metadata.get(file_id)
       if not file or not file["is_active"]:
           raise NotFoundException(f"file {file_id} is not found")
       return FileResponse(**file)
   
    def update(self,file_id:UUID,data:FileUpdate):
       file =_metadata.get(file_id)
       if not file or not file["is_active"]:
           raise NotFoundException(f"file id {file_id} is not found")
       
       updates=data.model_dump(exclude_none=True)
       file.update(updates)
       _metadata[file_id]=file
       return FileResponse(**file)
   
    def delete(self,file_id:UUID):
       file=_metadata.get(file_id)
       if not file or not file["is_active"]:
           raise NotFoundException(f"file id {file_id} is not found")
        
       file["is_active"]=False
       _metadata[id]=file 
       return FileResponse(**file)
       

filemetadata_services = FileMetaDataServices()