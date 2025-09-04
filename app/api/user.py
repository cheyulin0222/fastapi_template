from typing import Annotated
from fastapi import APIRouter
from fastapi.params import Depends
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.user import UserInfo

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/me", response_model=UserInfo)
def read_current_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user