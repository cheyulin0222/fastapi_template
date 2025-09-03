from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserInfo(BaseModel):
    username: str
    full_name: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
