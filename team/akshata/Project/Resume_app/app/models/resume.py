from pydantic import BaseModel,Field
from uuid import UUID , uuid4
from datetime import datetime

class ResumeRecord(BaseModel):
    id: UUID = Field(default_factory =uuid4 )
    student_name : str
    email : str
    original_filename : str
    filename : str
    content_type :str = "application/pdf"
    file_bytes : bytes
    uploaded_at : datetime = Field(default_factory =lambda:datetime.now() )
    file_size_bytes = int

    model_config = {"arbitrary_types_allowed= True"}
