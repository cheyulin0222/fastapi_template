from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    username: str = Field(
        ...,
        min_length=1,
        description="帳號",
        examples=["jeremy123"]
    )
    password: str = Field(
        ...,
        min_length=1,
        description="密碼",
        examples=["123"]
    )
    full_name: str = Field(
        min_length=1,
        description="名稱",
        examples=["殺氣A哲宇"]
    )

class RegisterResponse(BaseModel):
    message: str = "User registered successfully"
    isSuccess: bool = True

class LoginRequest(BaseModel):
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"



