from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.repository import user as user_repo


from app.schemas.user import UserCreate, UserLogin


def register_new_user(db: Session, user: UserCreate):
    db_user = user_repo.get_user_by_username(db, username=user.username)
    if db_user:
        return None

    hashed_password = get_password_hash(user.password)
    return user_repo.create_user(
        db,
        username=user.username,
        hashed_password=hashed_password,
        full_name=user.full_name
    )

def authenticate_user(db: Session, user_login: UserLogin):
    db_user = user_repo.get_user_by_username(db, username=user_login.username)
    if not db_user or not verify_password(user_login.password, db_user.hashed_password):
        return None
    return db_user