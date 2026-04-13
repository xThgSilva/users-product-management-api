from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.user.user_schemas import UserRequest, UserResponseBase, UsersListResponse
from typing import List
from services.user.user_service import create_user, get_all_users, get_user,delete_user_by_id, update_user_by_id

router = APIRouter()

@router.post("/register", status_code=201, response_model=UserResponseBase)
def register_user(user: UserRequest, db: Session = Depends(get_db)):
    new_user = create_user(user, db)

    return {
        "message": "User created.",
        "user": new_user
    }

@router.get("/all", response_model=UsersListResponse)
def find_all_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return {
        "message": "Users list.",
        "users": users
    }

@router.get("/find/{id}", response_model=UserResponseBase)
def find_user_by_id(id: int, db: Session = Depends(get_db)):
    user_found = get_user(id, db)

    return {
        "message": "User found.",
        "user": user_found
    }

@router.delete("/delete/{id}", status_code=204)
def delete_user(id: int, db: Session = Depends(get_db)):
    delete_user_by_id(id, db)

@router.put("/update/{id}", response_model=UserResponseBase)
def update_user( id: int, user: UserRequest,db: Session = Depends(get_db)):
    user_updated = update_user_by_id(id, db, user)

    return {
        "message": "User updated",
        "user": user_updated
    }