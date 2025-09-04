
from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import create_access_token
from app.schemas.auth import RegisterResponse, RegisterRequest, LoginResponse, LoginRequest
from app.service import user as user_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="註冊"
)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    db_user = user_service.create_user(db, request)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already registered"
        )
    return RegisterResponse()

@router.post(
"/login",
    summary="登入",
)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = user_service.authenticate_user(db, request)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_access_token(data={"sub": user.username})
    return LoginResponse(access_token=access_token)