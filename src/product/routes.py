from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from src.product.schema import ProductCreate, ProductRead, SeasonEnum
from src.product.crud import create_product, get_products_by_season, get_products, save_image_to_disk
from database import get_db
from typing import Optional

router = APIRouter()

UPLOAD_DIR = "uploads/images"


@router.post("/", response_model=ProductRead)
async def create_new_product(
    name: str,
    price: int,
    description: Optional[str] = None,
    category_id: int = None,
    is_special_offer: Optional[bool] = False,
    discount: Optional[int] = 0,
    sizes: Optional[str] = None,
    season: SeasonEnum = None,
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
):
    image_path = None
    if image:
        image_path = save_image_to_disk(image, upload_dir=UPLOAD_DIR)

    product_data = ProductCreate(
        name=name,
        price=price,
        description=description,
        category_id=category_id,
        is_special_offer=is_special_offer,
        discount=discount,
        sizes=sizes,
        season=season,
    )

    return create_product(db, product_data, image_path=image_path)


@router.get("/season/{season}", response_model=list[ProductRead])
def read_products_by_season(season: SeasonEnum, db: Session = Depends(get_db)):
    products = get_products_by_season(db, season)
    if not products:
        raise HTTPException(status_code=404, detail="No products found for this season")
    return products


@router.get("/", response_model=list[ProductRead])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products