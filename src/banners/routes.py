from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.banners.crud import create_banner, get_banners, get_banner, update_banner, delete_banner
from src.banners.schema import BannerCreate, BannerUpdate, BannerOut
from database import get_db
from typing import List

router = APIRouter(prefix="/banners", tags=["Banners"])

@router.post("/", response_model=BannerOut)
def create_new_banner(banner: BannerCreate, db: Session = Depends(get_db)):
    return create_banner(db, banner)

@router.get("/", response_model=List[BannerOut])
def read_banners(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_banners(db, skip=skip, limit=limit)

@router.get("/{banner_id}", response_model=BannerOut)
def read_banner(banner_id: int, db: Session = Depends(get_db)):
    banner = get_banner(db, banner_id)
    if not banner:
        raise HTTPException(status_code=404, detail="Banner not found")
    return banner

@router.put("/{banner_id}", response_model=BannerOut)
def update_existing_banner(banner_id: int, banner: BannerUpdate, db: Session = Depends(get_db)):
    updated_banner = update_banner(db, banner_id, banner)
    if not updated_banner:
        raise HTTPException(status_code=404, detail="Banner not found")
    return updated_banner

@router.delete("/{banner_id}", response_model=BannerOut)
def delete_existing_banner(banner_id: int, db: Session = Depends(get_db)):
    deleted_banner = delete_banner(db, banner_id)
    if not deleted_banner:
        raise HTTPException(status_code=404, detail="Banner not found")
    return deleted_banner