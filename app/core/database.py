from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.settings import settings

DATABASE_URL = settings.DATABASE_URL

# 建立 Connection Engine 管理連線池
engine = create_engine(DATABASE_URL)
# 建立一個可重複使用的 Session 物件產生器
# Session 像是 EntityManager
# 處理物件追蹤，哪些是新的，修改的、被刪除的
# 交易管理，管理多個連線
# ORM 操作
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
