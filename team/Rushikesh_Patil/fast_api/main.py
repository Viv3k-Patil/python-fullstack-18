from fastapi import FastAPI
from datetime import date

app = FastAPI()

@app.get("/today")
def today():
    return {"today date is ": str(date.today())}