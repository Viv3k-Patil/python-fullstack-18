
from fastapi import FastAPI,HTTPException


app = FastAPI(
    title = "Exception Project"
)

@app.get("/health")
def check_health():
    try:
        1/0
    except Exception as e:
        raise HTTPException(
            status_code = 400,
            detail= f"the error is {str(e)}"

        )
    return{
        "status": "Ok"
    }