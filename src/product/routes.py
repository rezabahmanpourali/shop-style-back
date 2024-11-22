from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from src.product.schema import ProductCreate, ProductRead
from src.product.crud import create_product, get_products_by_category, get_products
from database import get_db

router = APIRouter()

@router.post("/", response_model=ProductRead)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/category/{category_id}", response_model=list[ProductRead])
def read_products_by_category(category_id: int, db: Session = Depends(get_db)):
    products = get_products_by_category(db, category_id)
    if not products:
        raise HTTPException(status_code=404, detail="No products found in this category")
    return products

@router.get("/", response_model=list[ProductRead])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products