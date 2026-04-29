from fastapi import APIRouter, FastAPI
from pydantic import BaseModel


router = APIRouter()

# get user info
@app.get("/users")
def get_user():
    return {
        "Users":user
    }

# get info by user id
@app.get("/users/{user_id}")
def get_user_id(user_id : int):
    for u in user:
        if u["id"] == user_id:
          return {
             "users" : u
            }  
        return {"error": "user not found"

        }

# POST create new user
@app.post("/create_user")
def create_new_user(new_user : Users):
    user.append(new_user)
    return {
        "Message ": " User created successfully",
        "users_data" : new_user
        }