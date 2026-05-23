
from fastapi import FastAPI
from datetime import datetime
from datetime import date, time

app = FastAPI()

# Get todays date
@app.get("/todays_date")
def get_todays_date():
    return {
        "Today's date is" : str(date.today())

    }

# Get today's date and current time

@app.get("/today's_date_time")
def get_todays_date_time():
    return{
        "Todays date and time is " : str(datetime.today())
    }

# get todays current time
@app.get("/current_time")
def get_current_time():
    now = datetime.now().time()
    return{
        "Todays date and time is " : str(now)
    }