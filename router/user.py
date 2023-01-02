from fastapi import Depends, APIRouter, HTTPException, status
from database import SessionLocal
from sqlalchemy.orm import Session
from typing import List
from schemas.User import UserSchema
from schemas.UserLogin import UserLogin
from datetime import datetime
from pytz import timezone
from models import Users


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", tags=["users"])
async def get_total_users(db:Session=Depends(get_db)):
    return db.execute("SELECT * FROM user").all()
    

@router.get("/users/{id}", tags=["users"])
async def get_users_by_id(id:int, db:Session=Depends(get_db)):
    return db.execute("SELECT * FROM user WHERE user_id = %s" %id).fetchall()


@router.post("/users", response_model=UserSchema, tags=["users"], status_code=status.HTTP_201_CREATED)
def input_users(user: UserSchema, db:Session=Depends(get_db)):
    u = Users(
        nama = user.nama,
        email = user.email,
        password = user.password,
    )
    try:
        db.add(u)
        db.commit()
        return u
    except:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

@router.post("/users/login", tags=["users"], status_code=status.HTTP_201_CREATED)
def input_users(user: UserLogin, db:Session=Depends(get_db)):
    role = db.execute("SELECT user_id FROM user WHERE email = '%s' AND password = '%s'" %(user.email, user.password)).fetchone()
    try:
        for hasilrole in role:
            user_id = hasilrole
            return {"user_id" : user_id}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)    
    