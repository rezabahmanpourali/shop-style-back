from sqlalchemy.orm import Session
from src.auth.models import User 
from src. auth.schemas import UserCreate
from passlib.hash import bcrypt

def create_user(db: Session, user: UserCreate):
    password = bcrypt.hash(user.password)
    db_user = User(username=user.username, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()