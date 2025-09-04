from sqlalchemy.orm import Session
from app.core.security import get_password_hash, verify_password
from app.repository import user as user_repo
from app.schemas.auth import RegisterRequest, LoginRequest


def create_user(db: Session, request: RegisterRequest):
    db_user = user_repo.get_user_by_username(db, username=request.username)
    if db_user:
        return None

    hashed_password = get_password_hash(request.password)
    return user_repo.create_user(
        db,
        username=request.username,
        hashed_password=hashed_password,
        full_name=request.full_name
    )

def authenticate_user(db: Session, request: LoginRequest):
    db_user = user_repo.get_user_by_username(db, username=request.username)
    if not db_user or not verify_password(request.password, db_user.hashed_password):
        return None
    return db_user

