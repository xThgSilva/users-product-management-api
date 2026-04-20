from fastapi import HTTPException, Depends
from models.user.user_model import Users
from auth.security import verify_password
from auth.jwt_handler import create_access_token

def login_service(email, password, db):
    user = db.query(Users).filter(Users.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found with e-mail.")
    
    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials.")

    token = create_access_token({"id": user.id})

    return token
