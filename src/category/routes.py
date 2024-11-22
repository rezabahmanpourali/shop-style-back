from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from src.category.schema import CategoryCreate, CategoryRead
from src.category.curd import create_category, get_categories
from database import get_db

router = APIRouter()

@router.post("/", response_model=CategoryRead)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

@router.get("/", response_model=list[CategoryRead])
def read_all_categories(db: Session = Depends(get_db)):
    categories = get_categories(db)
    return categories