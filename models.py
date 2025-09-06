from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base 

# SQLAlchemy models for db tables
class User(Base): 
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    balance = Column(Float, defatult=0.0)

    transactions_sent = relationship("Transaction", foreign_keys="Transactions.sender_id")
    transactions_received = relationship("Transaction", foreign_keys="Transactions.receiver_id")

# Transaction model to record transactions between users.
class Transaction(Base): 
    __tablename__ = "transactions" 

    id = Column(Integer, primary_key=True, index=True) 
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())