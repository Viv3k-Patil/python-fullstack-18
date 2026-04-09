from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    is_active: bool = True
    address: Optional[str] = None

@app.post("/names")
def create_name(name_obj: User):
    return {"name": name_obj.name}