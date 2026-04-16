from fastapi import APIRouter
from app.schema.team_schema import Team
from app.db.db import teams
from app.services.team_service import create_team_service, get_all_teams_service, get_team_by_id_service, delete_team_by_id_service, update_team_service

router = APIRouter()

# POST create team 
@router.post("/teams")
def create_team(new_team: Team):
    return create_team_service(new_team)

# GET all teams
@router.get("/teams")
def get_all_teams():
    return get_all_teams_service();

# GET a team by id
@router.get("/teams/{team_id}")
def get_team_by_id(team_id: int):
    return get_team_by_id_service(team_id)

# DELETE a team by id
@router.delete("/teams/{team_id}")
def delete_team_by_id(team_id: int):
    return delete_team_by_id_service(team_id)
        
# PUT update team
@router.put("/teams/{team_id}")
def update_team(team_id: int, updated_team: Team):
    return update_team_service(team_id, updated_team)
