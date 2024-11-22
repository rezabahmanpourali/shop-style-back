from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
DATABASE_URL = "postgresql://root:gpFs9JiscHRZYqdIG2KmuOjR@logan.liara.cloud:33282/postgres"
SECRET_KEY = 'supersecretkey'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()