from sqlalchemy.orm import Session
from src.product.models import Product, Size, Season
from src.product.schema import ProductCreate

def create_product(db: Session, product: ProductCreate):
    season_names = [season.name for season in product.seasons] 
    seasons = db.query(Season).filter(Season.name.in_(season_names)).all()
    sizes = db.query(Size).filter(Size.id.in_(product.sizes)).all()

    db_product = Product(
        name=product.name,
        price=product.price,
        description=product.description,
        category_id=product.category_id,
        is_special_offer=product.is_special_offer,
        discount=product.discount,
        sizes=sizes,
        seasons=seasons,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products_by_category(db: Session, category_id: int):
    return db.query(Product).filter(Product.category_id == category_id).all()

def get_products(db: Session):
    return db.query(Product).all()