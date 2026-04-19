from fastapi import FastAPI

app=FastAPI(
    title="Interview-App",
    description=" simple interview Application Build with FastApi",
    version="1.1.0",
    docs_url="/docs"
    )
@app.get("/health")
def check_health():
    return {
        "msg" : "health is okk and server is running"
    }
