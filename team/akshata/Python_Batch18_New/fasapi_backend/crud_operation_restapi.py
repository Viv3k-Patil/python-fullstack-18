from fastapi import FastAPI

app = FastAPI()

users = ["user1","user2","user3"]

#get all users list
@app.get("/users")
def get_users():
    return {
            f"List Of all users" : users 
        }


#get user by id
@app.get("/users/{id}")
def get_id(id:int):
    return {
        "user":users[0]
    }

#create new user
@app.post("/users/{name}")
def create_user(name :str):
    users.append(name)
    return {
        "message": f"user {name} created successfully"
    }

#create new user with using query parameters
@app.post("/users")
def create_user_with_query_params(name : str):
    users.append(name)
    return {
        "users" : f"user {name} created sucessfully."
    }

#Delete user using id
@app.delete("users/{id}")
def delete_user(id:int):
    users.pop(id)
    return {
        "status" : "User deleted successfully..."    }