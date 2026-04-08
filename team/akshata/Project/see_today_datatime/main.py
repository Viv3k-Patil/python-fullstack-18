
from fastapi import FastAPI
from datetime import datetime
app = FastAPI()

# Get todays date and current time

@app.get("/todays_date")
def get_todays_date():
    return{
        "Todays date is " : datetime.today
    }
