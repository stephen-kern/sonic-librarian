# The connection betwenn our Python app and the database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import DATABASE_URL


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

# Base class for our ORM models
class Base(DeclarativeBase):
    pass

