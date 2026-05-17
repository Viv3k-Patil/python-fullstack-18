
from fastapi import FastAPI,HTTPException
from exceptions.app_exception import TeamNotFoundException

app = FastAPI(
    title = "Exception Project"
)

@app.get("/health")
def check_health():
    try:
        raise TeamNotFoundException("Team not found..!")
    except Exception as e:
        raise HTTPException(
           status_code= 400,
           detail = f"the error is {str(e)}"
       )
    return{
        "status": "Ok"
    }







