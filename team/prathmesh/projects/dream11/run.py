import uvicorn

if __name__ == "__main__":
    #app run code
    uvicorn.run( "app.main:app",reload=True)