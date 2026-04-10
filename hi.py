from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import random
import secrets


app = FastAPI(
  
    title="Arun API Service",
    description="This API Service Created By Arunkrishna",
    version="1.0.0"
)

otp_storage = {}


# Temporary database (list)
users = []



# Create User Model
class User(BaseModel):
    user_name: str
    user_id: int
    email: str
    city: str

#postmethod 

@app.post("/create_user", tags=["Users"])
def create_user(user: User):
 # generate random token
        token = secrets.token_hex(16)
        users.append(user)
        return {
        "message": "User created successfully",
        "token": token,
        "data": user
    }

# GET - GET All USERS
@app.get("/get_all_users",  tags=["Users"])
def get_users():
    return {
        "users": users
    }


# GET - GET USER BY USER ID 

@app.get("/get_user/{user_id}", tags=["Users"])
def get_user(user_id: int):
    for user in users:
        if user.user_id == user_id:
            return user
    return {"message": "User not found"}

# UPDATE USER
@app.put("/update_user/{user_id}",  tags=["Users"] )
def update_user(user_id: int, updated_user: User): 
    for index, user in enumerate(users):
        if user.user_id == user_id:
            users[index] = updated_user
            return {"message": "User updated successfully", "data": updated_user}

    raise HTTPException(status_code=404, detail="User not found")


# DELETE USER
@app.delete("/delete_user/{user_id}", tags=["Users"] )
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.user_id == user_id:
            deleted_user = users.pop(index)
            return {"message": "User deleted successfully", "data": deleted_user}
    raise HTTPException(status_code=404, detail="User not found")




















