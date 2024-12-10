from pydantic import BaseModel
from typing import Optional

class CategoryCreate(BaseModel):
    name: str
    parent_id: Optional[int] = None
    is_active: bool = True 

    class Config:
        orm_mode = True

class CategoryRead(BaseModel):
    id: int
    name: str
    parent_id: Optional[int] = None
    is_active: bool

    class Config:
        orm_mode = True

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    parent_id: Optional[int] = None
    is_active: Optional[bool] = None

    class Config:
        orm_mode = True