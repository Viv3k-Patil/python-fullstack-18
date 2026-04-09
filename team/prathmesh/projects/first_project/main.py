from fastapi import FastAPI

users=["user1","user2",
       "user3"]

app=FastAPI()

#get all users
@app.get("/users")
def get_users():
    return {
        "users" : users
    }

#get id of user
@app.get("/users/{id}")
def get_id(id:int):
    return {
        "user":users[id]
    }
#create new user
@app.post("/users/{name}")
def add_user(name:str): 
    users.append(name)
    return {
             "massage":f"user {name} is added in list"
            }
#create_user_with_query_param
@app.delete("/users{id}")
def delet_user(id:int):
    users.pop(id)
    return  {
        "status":"user deleted id succesfully"
    }




