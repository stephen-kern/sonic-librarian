from app.core.database import engine
from app.models import artist, list, artist_list
from app.core.database import Base

Base.metadata.create_all(bind=engine)
print("Tables created with timestamps and soft delete functionality.")