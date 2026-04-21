from app.schema.team_schema import Team
from app.db.db import teams

def create_team_service(new_team: Team):
    teams.append(new_team)
    return {
        "msg": "new team successfully created"
    }

def get_all_teams_service():
    return {
        "teams": teams
    }

def get_team_by_id_service(team_id: int):
    for team in teams:
        if team.id == team_id:
            return team
    return {
        "message": f"team with {team_id} not found"
    }

def delete_team_by_id_service(team_id: int):
    for team in teams:
        if team.id == team_id:
            teams.remove(team)
            return {
                "message": f"team with {team_id} successfully deleted"
            }
    return {
        "message": f"team with {team_id} not found"
    }

def update_team_service(team_id: int, updated_team: Team):
    for team in teams:
        if team.id == team_id:
            team.name = updated_team.name
            team.player = updated_team.player
            return {
                "message": "team has been successfully updated"
            }
    return {
        "message": f"team with {team_id} not found"
    }