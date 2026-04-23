from fastapi.responses import FastAPI,Request,JSONResponse
from pydantic import BaseModel

#Custom Exception (INDUSTRY LEVEL)
app=FastAPI()

#first step
class TeamNotFoundError(BaseModel):
    def __init__(self,team_id:int):
        self.team_id=team_id
        
#second step
@app.exception_handler(TeamNotFoundError)
def exception_handler(exc:TeamNotFoundError,request:Request):
    return JSONResponse(
        status_code=500,
        content={
            "success":"false",
            "msg":f"Team {exc.team_id} not found"
        }
    )

#third step:use it
def get_team_by_id(team_id:int):
    for team in team:
        if team.id==team_id:
            return team
        raise TeamNotFoundError(team_id)
        