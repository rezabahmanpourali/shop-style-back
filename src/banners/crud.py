from sqlalchemy.orm import Session
from src.banners.models import Banner
from src.banners.schema import BannerCreate, BannerUpdate

def create_banner(db: Session, banner: BannerCreate):
    banner_data = banner.dict()
    if 'image_url' in banner_data and banner_data['image_url']:
        banner_data['image_url'] = str(banner_data['image_url'])
    if 'link' in banner_data and banner_data['link']:
        banner_data['link'] = str(banner_data['link'])

    db_banner = Banner(**banner_data)
    db.add(db_banner)
    db.commit()
    db.refresh(db_banner)
    return db_banner

def get_banners(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Banner).offset(skip).limit(limit).all()

def get_banner(db: Session, banner_id: int):
    return db.query(Banner).filter(Banner.id == banner_id).first()

def update_banner(db: Session, banner_id: int, banner: BannerUpdate):
    db_banner = db.query(Banner).filter(Banner.id == banner_id).first()
    if not db_banner:
        return None
    
    update_data = banner.dict(exclude_unset=True)
    if 'image_url' in update_data and update_data['image_url']:
        update_data['image_url'] = str(update_data['image_url'])
    if 'link' in update_data and update_data['link']:
        update_data['link'] = str(update_data['link'])
    
    for key, value in update_data.items():
        setattr(db_banner, key, value)
    db.commit()
    db.refresh(db_banner)
    return db_banner

def delete_banner(db: Session, banner_id: int):
    db_banner = db.query(Banner).filter(Banner.id == banner_id).first()
    if db_banner:
        db.delete(db_banner)
        db.commit()
    return db_banner