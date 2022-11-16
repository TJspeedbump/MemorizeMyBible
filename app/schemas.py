from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    username: str
    password: str

class UserSignUp(BaseModel):
    name: str
    email: EmailStr
    password: str
    confirm_password: str

class VerseIn(BaseModel):
    verse: str

class VerseOut(BaseModel):
    verse: str