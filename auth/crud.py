from sqlalchemy.orm import Session
from . import models, schemas
from passlib.hash import bcrypt

def create_user(db: Session, user: schemas.UserCreate):
    password = bcrypt.hash(user.password)
    db_user = models.User(username=user.username, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user