
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from database import Base
import enum

class SeasonEnum(enum.Enum):
    spring = "spring"
    summer = "summer"
    autumn = "autumn"
    winter = "winter"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    discount = Column(Integer, default=0)
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    sizes = Column(String, nullable=True)
    season = Column(Enum(SeasonEnum, name="seasons_enum"), nullable=False)
    image_path = Column(String, nullable=True)
    is_special_offer = Column(Boolean, default=False)

    category = relationship("Category", back_populates="products")

    # models = relationship("ModelProduct", back_populates="product")

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from database import Base

# class Model(Base):
#     __tablename__ = "models"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     image_path = Column(String, nullable=False)
#     description = Column(String, nullable=True)

#     products = relationship("ModelProduct", back_populates="model")

# from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
# from database import Base

# class ModelProduct(Base):
#     __tablename__ = "model_products"

#     id = Column(Integer, primary_key=True, index=True)
#     model_id = Column(Integer, ForeignKey("models.id"), nullable=False)
#     product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

#     model = relationship("Model", back_populates="products")
#     product = relationship("Product", back_populates="models")


#     from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
# from sqlalchemy.orm import relationship
# from database import Base
# from sqlalchemy.types import Enum
# from src.product.enums import SeasonEnum

# class ProductColor(Base):
#     __tablename__ = "product_colors"

#     id = Column(Integer, primary_key=True, index=True)
#     product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
#     color_name = Column(String, nullable=False)
#     color_code = Column(String, nullable=True)

#     product = relationship("Product", back_populates="colors")
#     sizes = relationship("ProductSize", back_populates="color", cascade="all, delete-orphan")


# class ProductSize(Base):
#     __tablename__ = "product_sizes"

#     id = Column(Integer, primary_key=True, index=True)
#     color_id = Column(Integer, ForeignKey("product_colors.id"), nullable=False)
#     size = Column(String, nullable=False)
#     quantity = Column(Integer, default=0)

#     color = relationship("ProductColor", back_populates="sizes")


# class Product(Base):
#     __tablename__ = "products"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     price = Column(Integer, nullable=False)
#     discount = Column(Integer, default=0)
#     description = Column(String, nullable=True)
#     category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
#     model = Column(String, nullable=True)
    # is_special_offer = Column(Boolean, default=False)
#     season = Column(Enum(SeasonEnum, name="seasons_enum"), nullable=False)
#     image_path = Column(String, nullable=True)

#     colors = relationship("ProductColor", back_populates="product", cascade="all, delete-orphan")
#     category = relationship("Category", back_populates="products")