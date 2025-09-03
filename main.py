import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.api import router as api_router
from app.core.database import Base, engine
from app.core.settings import settings
from app.exceptions.handler import http_exception_handler

# 建立資料表
# 生產環境可不需要
Base.metadata.create_all(bind=engine)

# 建立應用程式實例
app = FastAPI(
    title="FastAPI Template",
    description="A simple API server with auth and user management",
    version="1.0.0"
)

# 註冊 CORS 中間件
app.add_middleware(
    CORSMiddleware, # type: ignore
    allow_origins=settings.CORS_ORIGINS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    max_age=settings.CORS_MAX_AGE
)


# 註冊路由
app.include_router(api_router)

# 註冊例外處理
app.add_exception_handler(HTTPException, http_exception_handler) # type: ignore

# 啟動 Uvicorn 伺服器。它會監聽指定的 host 和 port，並運行你的 main:app
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.APP_RELOAD,
        workers=settings.UVICORN_WORKERS,
        timeout_keep_alive=settings.UVICORN_TIMEOUT_KEEP_ALIVE
    )
