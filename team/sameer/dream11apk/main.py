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