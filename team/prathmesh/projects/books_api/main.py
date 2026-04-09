# from fastapi import FastAPI
# from datetime import date
# app = FastAPI()

# books=[]
# @app.get("/books")  
# def get_books():
#     return {
#         "books" : books
#     }

# @app.get("/today")
# def today():
#     return {
#         "today": str(date.today())
#     }

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# models
class User(BaseModel):
    id: int
    username: str
    teams: list[str]

# in memory db
user = [
]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    return {"users": user}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for u in user:
        if u["id"] == user_id:
            return {"user": u}
    return {"error": "User not found"}

@app.post("/users")
def create_user(new_user: User):
    user.append(new_user)
    return {
        "message": "User created successfully", 
        "user": new_user
    }