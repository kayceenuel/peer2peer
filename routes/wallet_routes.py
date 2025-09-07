from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from database import get_db
from models import User, Transaction
from routes.auth_routes import get_current_user

router = APIRouter() 

@router.get("/balance")
def get_balance(current_user: User = Depends(get_current_user)): 
    return {"balance": current_user.balance}