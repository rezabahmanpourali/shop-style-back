from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Banner(Base):
    __tablename__ = "banners"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    link = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)