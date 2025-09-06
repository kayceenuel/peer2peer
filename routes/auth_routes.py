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
 
