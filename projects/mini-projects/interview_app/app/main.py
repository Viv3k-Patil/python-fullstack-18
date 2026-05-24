from fastapi import FastAPI, Request
from app.routes.interview_routes import router as interview_router
from app.exceptions.handler import global_exception_handler


app = FastAPI(
    title="Interview App",
    description="A simple interview application built with FastAPI.",
    version="1.0.0",
    docs_url="/docs",
) 

global_exception_handler(app)
app.include_router(interview_router)



@app.get("/health")
def health_check():
    return {"status": "ok"}