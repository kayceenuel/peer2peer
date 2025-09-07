from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from database import get_db
from models import User, Transaction
from routes.auth_routes import get_current_user

router = APIRouter() 

@router.get("/balance")
def get_balance(current_user: User = Depends(get_current_user)): 
    return {"balance": current_user.balance}

@router.post("/send")
def send_money(
    receiver_email: str,
    amount: float,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")

    if current_user.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    receiver = db.query(User).filter(User.email == receiver_email).first()
    if not receiver:
        raise HTTPException(status_code=404, detail="Receiver not found")

    # Update balances
    current_user.balance -= amount
    receiver.balance += amount

    transaction = Transaction(sender_id=current_user.id, receiver_id=receiver.id, amount=amount)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return {
        "msg": f"Sent {amount} to {receiver.email}",
        "transaction_id": transaction.id,
        "balance": current_user.balance,
    }

@router.get("/transactions")
def transaction_history(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    sent = db.query(Transaction).filter(Transaction.sender_id == current_user.id).all()
    received = db.query(Transaction).filter(Transaction.receiver_id == current_user.id).all()

    return {
        "sent": [{"to": tx.receiver_id, "amount": tx.amount, "timestamp": tx.timestamp} for tx in sent],
        "received": [{"from": tx.sender_id, "amount": tx.amount, "timestamp": tx.timestamp} for tx in received],
    }