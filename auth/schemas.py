from pydantic import BaseModel
class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    
    class Config:
        orm_mode = True

        
from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str