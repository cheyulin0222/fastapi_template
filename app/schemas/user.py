from pydantic import BaseModel, Field

class UserInfo(BaseModel):
    username: str
    full_name: str


