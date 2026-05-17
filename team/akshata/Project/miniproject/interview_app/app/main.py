
from fastapi import FastAPI

app = FastAPI(
      title = "Interview app",
      description = "A simple interview application built with FastAPI",
      version = "1.0.0",
      docs_url = "/docs",

)

@app.get("/health")
def check_health():
    return{
        "status": "Ok"
    }




