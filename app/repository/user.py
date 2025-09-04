from sqlalchemy.orm import Session
from app.models.user import User


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first() # type: ignore

def create_user(db: Session, username: str, hashed_password: str, full_name: str):
    db_user = User(username=username, hashed_password=hashed_password, full_name=full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user