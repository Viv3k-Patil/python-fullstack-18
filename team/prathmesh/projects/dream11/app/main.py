# from fastapi import FastAPI
# from pydantic import BaseModel, Field
# from typing import Optional, List

# app = FastAPI()

# # models
# class Team(BaseModel):
#     id: int
#     name: str = Field(min_length=3, max_length=50)
#     players: list[str] = [] 

# class User(BaseModel):
#     id: int
#     username: str = Field(min_length=3, max_length=20)
#     teams: List[str] = []
#     age: int = Field(gt=13, lt=100)
#     credit: Optional[float] = 0.0

# # in memory db
# user = [
# ]
# team = [
# ]

# @app.get("/health")
# def health_check():
#     return {"status": "ok"}

# @app.get("/users")
# def get_users():
#     return {"users": user}

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     for u in user:
#         if u["id"] == user_id:
#             return {"user": u}
#     return {"error": "User not found"}

# @app.post("/users")
# def create_user(new_user: User):
#     user.append(new_user)
#     return {
#         "message": "User created successfully", 
#         "user": new_user
#     }


# @app.get("/teams")
# def get_teams():
#     return {"teams": team}

# @app.post("/teams")
# def create_team(new_team: Team):
#     team.append(new_team)
#     return {
#         "message": "Team created successfully", 
#         "team": new_team
#     }


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# in memory database
teams = []

# models
class Team(BaseModel):
    id: int
    name: str = Field(example="My dream team", description="Enter team name", min_length=3, max_length=20)
    player: str


@app.get("/health")
def check_health():
    return {
        "status": "server is up and running"
    }

# POST create team 
@app.post("/teams")
def create_team(new_team: Team):
    teams.append(new_team)
    return {
        "msg": "new team successfully created"
    }

# GET all teams
@app.get("/teams")
def get_all_teams():
    return {
        "teams": teams
    }

# GET a team by id
@app.get("/teams/{team_id}")
def get_team_by_id(team_id: int):
    for team in teams:
        if team.id == team_id:
            return {
                "team": team
            }

# DELETE a team by id
@app.delete("/teams/{team_id}")
def delete_team_by_id(team_id: int):
    for team in teams:
        if team.id == team_id:
            teams.remove(team)
            return {
                "message": f"team with {team_id} successfully deleted"
            }
        
# PUT update team
@app.put("/teams/{team_id}")
def update_team(team_id: int, updated_team: Team):
    for team in teams:
        if team.id == team_id:
            team.name = updated_team.name
            team.player = updated_team.player
            return {
                "message": "team has been successfully updated"
            }


# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# teams=[]

# class Team(BaseModel):
#     id:int
#     name:str = Field(example="my dream team",description="enter team name",min_length=3,max_length=20)
#     player:str

# @app.get("/health")
# def check_helth():
#     return {
#         "status": "server is ok and running"
#     }
# @app.post("/teams")
# def create_team(new_team:Team):
#     teams.append(new_team)
#     return {
#         "msg":"new team succesfully created"
#     }
# @app.get("/teams")
# def get_all_teams():
#     return {
#         "show" : teams  
#     }

# # GET a team by id
# @app.get("/teams/{team_id}")
# def get_team_by_id(team_id: int):
#     for team in teams:
#         if team.id == team_id:
#             return {
#                 "team": team
#             }      
        
# #DELET team by id
# @app.delete("/teams/{team_id}")    
# def delete_team_by_id(team_id:int):
#     for team in teams:
#         if team.id == team_id:
#             return {
#                 "msg" : f"team deleted {team_id} succesfully"
#             }   

# #UPDATE team by id & name
# @app.put("/teams/{team_id}")
# def update_team(team_id:int,updated_team:Team):    
#     for team in teams:
#         if team.id == team_id:
#             team.name = updated_team.name
#             team.player = updated_team.player
#             return {
#                 "msg" : "team updated succesfully"
#             }
                
# class Item(BaseModel):
#     product_name: str
#     price: float

# class Order(BaseModel):
#     order_id: int
#     items: List[Item]  # A list of Item objects

# data = {
#     "order_id": 99,
#     "items": [
#         {"product_name": "Laptop", "price": 1200.50},
#         {"product_name": "Mouse", "price": 25.00}
#     ]
# }