from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class ArtistList(Base):
    __tablename__ = "artist_list"

    artist_id: Mapped[int] = mapped_column(
        ForeignKey("artists.id"),
        primary_key=True
    )

    list_id: Mapped[int] = mapped_column(
        ForeignKey("lists.id"),
        primary_key=True
    )