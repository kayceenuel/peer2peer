from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from database import get_db
from models import User, Transaction
from routes.auth_routes import get_current_user

router = APIRouter() 

@router.get("/balance")
def get_balance(current_user: User = Depends(get_current_user)): 
    return {"balance": current_user.balance}

@router.post("/transfer")
def send_money(
    receiver_email: str, 
    amount: float, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user) 
):

