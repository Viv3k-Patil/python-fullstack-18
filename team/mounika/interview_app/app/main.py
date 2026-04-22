from fastapi import FastAPI

app = FastAPI(
    title = "interview_app",
    decription = "A simple interview app with fastapi",
    version = "1.0.0",
    docs_url = "/docs"

)

#creating health endpoint
@app.get("/health")

def health_check():
    return{
        "status": "server is up and running"
    }
