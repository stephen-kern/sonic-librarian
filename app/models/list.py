from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.core.database import Base
from app.models.artist_list import ArtistList
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.artist import Artist

class List(Base):
    __tablename__ = "lists"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    artists: Mapped[list["Artist"]] = relationship(
        secondary="artist_list",
        back_populates="lists"
    )