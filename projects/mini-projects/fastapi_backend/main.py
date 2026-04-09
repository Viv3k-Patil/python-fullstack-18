from fastapi import FastAPI, Request

app = FastAPI()

users = ["user1", "user2", "user3"]

@app.get("/health")
def health_check():
    return {"status": users[0]}

# get all users
@app.get("/users")
def get_users():
    return {
        "users": users
    }

# get user by id
@app.get("/users/{id}")
def get_user(id: int):
    return {
        "user": users[id]
    }

# create new user
@app.post("/users/{name}")
def create_user(name: str):
    users.append(name)
    return {
        "message": f"User {name} created successfully"
    }

@app.post("/users")
def create_user_with_query_param(name: str):
    users.append(name)
    return {
        "message": f"User {name} created successfully"
    }


# delete user
@app.delete("/users/{id}")
def delete_user(id: int):
    users.pop(id)
    return {"status": "user deleted successfully"}


# print(app.routes)