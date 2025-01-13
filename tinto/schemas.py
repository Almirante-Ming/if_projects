from pydantic import BaseModel, EmailStr

class Message(BaseModel):
    message: str
    
class User_Schema(BaseModel):
    username: str
    email: EmailStr
    passphase: str
    
class User_public(BaseModel):
    username: str
    email: EmailStr