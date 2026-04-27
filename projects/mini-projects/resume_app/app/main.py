from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import Response, FileResponse
from app.routers.resume_router import router as resume_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(resume_router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
def show_frontend():
    return FileResponse("static/index.html")
