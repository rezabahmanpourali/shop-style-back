from pydantic import BaseModel, HttpUrl
from typing import Optional, List

class BannerBase(BaseModel):
    title: str
    image_url: HttpUrl
    link: Optional[HttpUrl]
    is_active: Optional[bool] = True

class BannerCreate(BannerBase):
    pass

class BannerUpdate(BannerBase):
    pass

class BannerOut(BannerBase):
    id: int

    class Config:
        orm_mode = True