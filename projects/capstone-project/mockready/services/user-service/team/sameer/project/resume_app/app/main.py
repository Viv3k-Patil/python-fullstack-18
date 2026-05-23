from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from app.routers.resume_router import router as resume_router
from fastapi.staticfiles import StaticFiles
from app.exceptions.global_exception_handler import global_exception_handler

app = FastAPI()

# --------------------------------------------------------
# Register global exception handler
# --------------------------------------------------------
global_exception_handler(app)

app.include_router(resume_router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
def show_frontend():
    return FileResponse("static/index.html")