from passlib.context import CryptContext
import os 
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Token expiration time in minutes 
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # Refresh token expiration time in mintes (7 days)

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str: 
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool: 
    return password_context.verify(password, hashed_password) 