# The connection between our Python app and the database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL
from app.models.base import Base
from typing import Generator
from sqlalchemy.orm import Session


# Engine and SessionLocal are the core components for database interaction
engine = create_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try: 
        yield db # hands the session to fastAPI
    finally:
        db.close() # cleans up the session after use