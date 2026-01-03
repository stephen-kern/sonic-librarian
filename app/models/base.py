from  sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped
from sqlalchemy import Column, Boolean, DateTime, func, Integer

class Base(DeclarativeBase):
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    is_deleted: Mapped[bool] = Column(Boolean, default=False, nullable=False)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"