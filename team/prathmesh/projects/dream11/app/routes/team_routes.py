from fastapi import APIRouter
from app.schema.team_schema import Team
from app.db.db import teams

router=APIRouter()

# POST create team 
@router.post("/teams")
def create_team(new_team: Team):
    teams.append(new_team)
    return {
        "msg": "new team successfully created"
    }

# GET all teams
@router.get("/teams")
def get_all_teams():
    return {
        "teams": teams
    }

# GET a team by id
@router.get("/teams/{team_id}")
def get_team_by_id(team_id: int):
    for team in teams:
        if team.id == team_id:
            return {
                "team": team
            }

# DELETE a team by id
@router.delete("/teams/{team_id}")
def delete_team_by_id(team_id: int):
    for team in teams:
        if team.id == team_id:
            teams.remove(team)
            return {
                "message": f"team with {team_id} successfully deleted"
            }
        
# PUT update team
@router.put("/teams/{team_id}")
def update_team(team_id: int, updated_team: Team):
    for team in teams:
        if team.id == team_id:
            team.name = updated_team.name
            team.player = updated_team.player
            return {
                "message": "team has been successfully updated"
            }
