from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Generator

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database Url is:", SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SESSIONLOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db() -> Generator:
    
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()
