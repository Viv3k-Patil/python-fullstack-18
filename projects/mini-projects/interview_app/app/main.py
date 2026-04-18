from fastapi import FastAPI


app = FastAPI(
    title="Interview App",
    description="A simple interview application built with FastAPI.",
    version="1.0.0",
    docs_url="/docs",
) 

@app.get("/health")
def health_check():
    return {"status": "ok"}