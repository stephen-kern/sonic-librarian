from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

app = FastAPI(
    title="Sonic Librarian",
    description="A fast and efficient music library manager.",
    version="0.1.0"
)

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    # If DB connection fails, this endpoing fails
    return {"status": "ok"}
