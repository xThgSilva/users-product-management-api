from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from services.auth.auth_service import login_service

router = APIRouter(tags=["Auth"])

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    token = login_service(email, password, db)

    return {
        "message": "Logged in succesfully",
        "access_token": token
    }