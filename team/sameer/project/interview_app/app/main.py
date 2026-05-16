from fastapi import FastAPI   
from app.routes.interview_routes import router as interview_router
from app.exeptions.handler import global_exception_handler
app = FastAPI(
     title = " Interview App",
     description = "Simple interview application",
     version = "1.0.0"

)
app.include_router(interview_router)
global_exception_handler(app)

@app.get("/health")
def health_check():
    return {"status : ok"}
