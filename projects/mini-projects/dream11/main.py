from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

# models
class Team(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=50)
    players: list[str] = [] 

class User(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=20)
    teams: List[str] = []
    age: int = Field(gt=13, lt=100)
    credit: Optional[float] = 0.0

# in memory db
user = [
]
team = [
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


@app.get("/teams")
def get_teams():
    return {"teams": team}

@app.post("/teams")
def create_team(new_team: Team):
    team.append(new_team)
    return {
        "message": "Team created successfully", 
        "team": new_team
    }