from models.user.user_model import Users
from fastapi import HTTPException

def create_user(user, db):
    user_existing = db.query(Users).filter(Users.email == user.email).first()

    if user_existing:
        raise HTTPException(status_code=409, detail= "This e-mail is already registered")
    else:
        new_user = Users(name=user.name, email=user.email, password=user.password)

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

def get_all_users(db):
    return db.query(Users).all()

def get_user(id, db):
    user_found = db.query(Users).filter(Users.id == id).first()

    if user_found:
        return user_found
    else:
        raise HTTPException(status_code=404, detail= f"User with Id {id} not found.")