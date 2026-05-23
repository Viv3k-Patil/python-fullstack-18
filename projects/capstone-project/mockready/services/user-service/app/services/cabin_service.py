from uuid import UUID,uuid4

from app.schemas.cabin import CreateCabin,CabinResponse,UpdateCabin
from app.core.exceptions import NotFoundException,ConflictException

_cabin: dict[UUID,dict]={}

class CabinService:
    def create(self,data:CreateCabin)->CabinResponse:
        #buissnes rule no duplicate cabin_id
        for c in _cabin.values():
            if c["cabin_number"] == data.cabin_number:
                raise ConflictException(f"cabin number {data.cabin_number} is alreday exists")
          
        cabin= {
                "id":uuid4(),
                "campus_id":data.campus_id,
                "cabin_number":data.cabin_number,
                "is_active":True,
            }     
        
        _cabin[cabin["id"]]=cabin   
        return CabinResponse(**cabin)
    
    def get_all(self,page:int ,size:int)->tuple[list[CabinResponse],int]:
        active  = [c for c in _cabin.values() if c["is_active"]]
        total   = len(active)
        start   = (page-1)*size
        chunks  = active[start:start+size]
        return[CabinResponse(**c) for c in chunks],total
    
    def get_by_id(self,cabin_id:UUID):
        cabin=_cabin.get(cabin_id)
        if not cabin or not cabin["is_active"]:
            raise NotFoundException(f"cabin id {cabin_id} not found")
        return CabinResponse(**cabin)
    
    def update(self,cabin_id:UUID,data:UpdateCabin)->CabinResponse:
        cabin=_cabin.get(cabin_id)
        if not cabin or not cabin["is_active"]:
            raise NotFoundException(f"cabin id {cabin_id} not found")
        
        # only update fields the client actually sent
        updates=data.model_dump(exclude_none=True)
        cabin.update(updates)
        _cabin["cabin_id"]=cabin
        return CabinResponse(**cabin)
    
    
    def delete(self, cabin_id: UUID):
        cabin=_cabin.get(cabin_id)
        if not cabin or not cabin["is_active"]:
            raise NotFoundException(f"cabin id {cabin_id} not found")
        
        #always soft delete never remove in db 
        cabin["is_active"]=False
        return CabinResponse(**cabin)
    
cabin_services=CabinService()    
        
        