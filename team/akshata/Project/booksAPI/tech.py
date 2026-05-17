from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str              # required
    age: int = 18          # default
    city: Optional[str] = None   # optional