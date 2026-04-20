from fastapi import FastAPI

app = FastAPI(
     title = " Interview App",
     description = "Simple interview application",
     version = "1.0.0"

)

@app.get("/health")
def health_check():
    return {"status : ok"}
