from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class Seasons(str, Enum):
    spring = "spring"
    summer = "summer"
    autumn = "autumn"
    winter = "winter"

class SizeType(str, Enum):
    clothing = "clothing"
    shoes = "shoes"

class SizeBase(BaseModel):
    value: str
    size_type: SizeType

class SizeRead(SizeBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    price: int
    description: Optional[str] = None
    category_id: int
    is_special_offer: Optional[bool] = False
    discount: Optional[int] = 0

class ProductCreate(ProductBase):
    sizes: List[int]  
    seasons: List[Seasons] 

class ProductRead(ProductBase):
    id: int
    sizes: List[SizeRead] 
    seasons: List[Seasons]

    class Config:
        orm_mode = True