from fastapi import FastAPI
from pydantic import BaseModel , Field
from typing import Optional



app = FastAPI()

# Model
class Users(BaseModel):
    id : int
    username : str = Field(min_length=3 , max_length= 20)  #required
    team : list[str] = [] #default
    age : Optional[int]   #optional


# in memory db
user = []
team = []


# get check health status
@app.get("/health")
def check_health():
    return{
        "Status": "Ok"
    }

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

#check age criteriya
@app.post("/check_age")
def check_age(person: Users):
    return {
        "Message":f"{person.username} age is valid",
        "check_age": person.age

    }

