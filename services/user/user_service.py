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
    
def delete_user_by_id(id, db):
    user_to_delete = db.query(Users).filter(Users.id == id).first()

    if user_to_delete:
        db.delete(user_to_delete)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail= f"User with Id {id} not found")
    
def update_user_by_id(id, db, user):
    user_to_update = db.query(Users).filter(Users.id == id).first()

    if user_to_update:
        user_to_update.nome = user.nome
        user_to_update.email = user.email

        db.commit()
        db.refresh(user_to_update)

        return user_to_update
    else:
        raise HTTPException(status_code=404, detail= f"User with Id {id} not found to update")
