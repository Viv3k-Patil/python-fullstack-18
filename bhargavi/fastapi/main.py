from fastapi import FastAPI

app = FastAPI()

@app.get("/health-check")
def check_health():
    return {"status":"Health is OK"}

@app.get("/hello")
def get_mesg():
    return {"mesg":"Hello fastapi"}


@app.get("/about")
def about():
    return {"info":"This is my first Fastapi project"}
