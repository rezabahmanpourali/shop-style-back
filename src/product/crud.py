import os
from sqlalchemy.orm import Session
from src.product.models import Product
from src.product.schema import ProductCreate, SeasonEnum
from fastapi import UploadFile
from typing import Optional
import uuid


def save_image_to_disk(image: UploadFile, upload_dir: str = "uploads/images") -> str:
    os.makedirs(upload_dir, exist_ok=True)

    ext = os.path.splitext(image.filename)[-1]
    safe_filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(upload_dir, safe_filename)

    with open(file_path, "wb") as buffer:
        buffer.write(image.file.read())

    return file_path


def create_product(db: Session, product: ProductCreate, image_path: Optional[str] = None):
    db_product = Product(
        name=product.name,
        price=product.price,
        description=product.description,
        category_id=product.category_id,
        is_special_offer=product.is_special_offer,
        discount=product.discount,
        sizes=product.sizes,
        season=product.season,
        image_path=image_path,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products_by_season(db: Session, season: SeasonEnum):
    return db.query(Product).filter(Product.season == season).all()


def get_products(db: Session):
    return db.query(Product).all()