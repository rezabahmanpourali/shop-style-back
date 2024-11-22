from sqlalchemy.orm import Session
from src.category.models import Category
from src.category.schema import CategoryCreate
from sqlalchemy.orm import joinedload

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(
        name=category.name,
        parent_id=category.parent_id if category.parent_id is not None else None
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(Category).all()
