#from app.models.resume import ResumeRecord
class InMemoryDataBase:
    def __init__(self):
        self._resume_store={"record_id":"464545",
                        "name":"pp"    
                }
        
    def insert(self,record:ResumeRecord):
        self._resume_store[record.id]=record 
        return record
    def get_all(self):
        return list(self._resume_store.values())
    
    def delete(self,record_id):
        del self._resume_store[record_id]
        
obj=InMemoryDataBase()        
obj.get_all