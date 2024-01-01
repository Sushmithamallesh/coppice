from typing import List
from fastapi import APIRouter, Body, HTTPException, Request
from .schemas import UserBase, UserDisplay

from database import mongo

router = APIRouter()

@router.get("/users", response_model=List[UserDisplay])
def get_users():
    users = mongo.db.get_collection('users').find()
    return [UserDisplay.model_validate(**user) for user in users]

@router.get("/user/{email}", response_model=UserDisplay)
def get_user(email: str):
    if not email or "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid or missing email")
    user = mongo.db.get_collection('users').find_one({'email': email})
    if user:
        return UserDisplay(**user, id=str(user['_id']))
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/user", response_model=UserDisplay)
def add_user(user: UserBase):
    try:
        if check_if_user_exists(email=user.email):
            raise HTTPException(status_code=400, detail="User already exists")
        result = mongo.db.get_collection('users').insert_one(user.model_dump(by_alias=True))
        user_id = str(result.inserted_id)
        return UserDisplay(**user.model_dump(by_alias=True), id=user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add user: {e}")
        
def check_if_user_exists(email:str) -> bool:
    user = mongo.db.get_collection('users').find_one({'email': email})
    return bool(user)
