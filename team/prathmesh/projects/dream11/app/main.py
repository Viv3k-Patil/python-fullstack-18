
from fastapi import FastAPI
from app.routes.team_routes import router as team_router

app = FastAPI()

app.include_router(team_router)


@app.get("/health")
def check_health():
    return {
        "status": "server is up and running"
    }

