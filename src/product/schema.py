from fastapi import UploadFile, File
from pydantic import BaseModel
from typing import Optional
from enum import Enum


class SeasonEnum(str, Enum):
    spring = "spring"
    summer = "summer"
    autumn = "autumn"
    winter = "winter"


class ProductBase(BaseModel):
    name: str
    price: int
    description: Optional[str] = None
    category_id: int
    is_special_offer: Optional[bool] = False
    discount: Optional[int] = 0
    sizes: Optional[str] = None
    season: SeasonEnum


class ProductCreate(ProductBase):
    image: Optional[UploadFile] = None


class ProductRead(ProductBase):
    id: int
    image_path: Optional[str] = None

    class Config:
        orm_mode = True