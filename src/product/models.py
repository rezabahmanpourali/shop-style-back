from sqlalchemy import (
    Column, Integer, String, ForeignKey, Float, Boolean, Table, Enum
)
from sqlalchemy.orm import relationship
from database import Base
import enum

class SizeType(enum.Enum):
    CLOTHING = "clothing"
    SHOES = "shoes" 

class SeasonEnum(enum.Enum):
    spring = 'spring'
    summer = 'summer'
    autumn = 'autumn'
    winter = 'winter'


product_season_association = Table(
    "product_season_association",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True),
    Column("season_id", Integer, ForeignKey("seasons.id"), primary_key=True)
)


class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(SeasonEnum, name="seasons_enum"), nullable=False, unique=True)  

    products = relationship(
        "Product", secondary=product_season_association, back_populates="seasons"
    )

class Size(Base):
    __tablename__ = "sizes"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(String, nullable=False) 
    size_type = Column(Enum(SizeType), nullable=False) 

    products = relationship("Product", secondary="product_size_association", back_populates="sizes")

product_size_association = Table(
    "product_size_association",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True),
    Column("size_id", Integer, ForeignKey("sizes.id"), primary_key=True)
)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    discount = Column(Integer, default=0) 
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    model = Column(String, nullable=True)
    is_special_offer = Column(Boolean, default=False)

    category = relationship("Category", back_populates="products")
    seasons = relationship(
        "Season", secondary=product_season_association, back_populates="products"
    )
    sizes = relationship(
        "Size", secondary=product_size_association, back_populates="products"
    )