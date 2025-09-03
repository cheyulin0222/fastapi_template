import uvicorn
from fastapi import FastAPI, HTTPException

from app.api import auth, user
from app.core.database import Base, engine
from app.exceptions.handler import http_exception_handler

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Template",
    description="A simple API server with auth and user management",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(user.router)

app.add_exception_handler(HTTPException, http_exception_handler) # type: ignore

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
