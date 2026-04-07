
from fastapi import FastAPI

app = FastAPI()

books = ["python","FastAPIS"]

# health end point
@app.get("/health")
def get_health():
    return {
        "Status": "Health is okk"
    }

# get all books
@app.get("/books")
def get_books():
    return {
        "data ": books
    }

# get particular with an id
@app.get("/books/{id}")
def get_book_by_id(id : int):
    return{
        "data" : books[id]
    }

# create new book
@app.post("/books/{name}")
def create_books(name : str):
    books.append(name)
    return{
        "data": f"create books {name} successfully."
    }

#delete books name using id
@app.delete("/books/{id}")
def delete_book_id(id : int):
    books.pop(id)
    return {
        "Data": f"Delete books successfully"
    }
