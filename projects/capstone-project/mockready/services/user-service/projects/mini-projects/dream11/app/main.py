from fastapi import FastAPI
from app.routes.team_routes import router as team_router

app = FastAPI(
    title="Dream11 API",
    description="API for managing teams in Dream11",
    version="1.0.0",
    docs_url="/api/docs"
)

app.include_router(team_router)

@app.get("/health", status_code=201)
def health_check():
    return {"status": "ok"}
