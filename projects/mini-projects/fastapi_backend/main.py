from fastapi import FastAPI

app =  FastAPI()

@app.get("/hello")
def say_hello():
    return{"msg" : "Hello"}

@app.get("/health-check")
def check_health():
    return {"Pornima" : "Parshetti"}

