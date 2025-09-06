from fastapi import APIRouter, Depends, HTTPException, status  # Import modules from FastAPI
from sqlalchemy.orm import Session
from pydantic import BaseModel 
from database import get_db
from models import User 
from auth import get_hashed_password, verify_password, create_access_token, create_refresh_token # import auth functions 

router = APIRouter() #Define a router for auth related routes 

# pydantic models for request and reponse bodies
class UserCreate(BaseModel): 
    username: str 
    email: str 
    password: str 

class UserLogin(BaseModel):
    username: str 
    pasword: str
 

def signup(user: UserCreate, db: Session = Depends(get_db)): 
    #Check if user with same username or email already exists 
    db_user = db.query(User).filter(User.email == user.email).first() 
    if db_user: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Email already registered")
    
    hashed_password = get_hashed_password(user.password)
    new_user = User(
        username=user.username, # 
        email=user.email, 
        password_hash=hashed_password, 
        balance=0.0 #initial balance set to 0.0
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 

    return {"msg": "User created sucesfully", "user_id": new_user.id} 