from fastapi import APIRouter, Depends, HTTPException
from src.auth import schemas, crud, jwt
from src.auth.models import User
from sqlalchemy.orm import Session
from database import get_db
from src.auth.jwt import pwd_context,get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = crud.create_user(db=db, user=user)

    access_token = jwt.create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = form_data.username
    password = form_data.password

    db_user = db.query(User).filter(User.username == username).first()
    if not db_user or not pwd_context.verify(password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = jwt.create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/user")
async def read_user(current_user: User = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "created_at": current_user.id,
    }