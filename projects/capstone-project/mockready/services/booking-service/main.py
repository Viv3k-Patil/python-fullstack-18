from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="Booking Service")

app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": "Booking Service Running"}