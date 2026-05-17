from fastapi import FastAPI

app = FastAPI()

users = []

@app.get("/health")
def health_check():
    return {"status": "Server is up and running"}