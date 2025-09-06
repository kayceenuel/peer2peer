from pydantic import BaseModel, EmailStr 

# Pydantic models for request and reponse bodies 
class UserCreate(BaseModel):  # Model for user creation
    username: str 
    email: EmailStr
    password: str 

class UserResponse(BaseModel): # Model for user reponse
    id: int 
    username: str
    email: EmailStr 
    balance: float

    class Config:
        orm_mode = True