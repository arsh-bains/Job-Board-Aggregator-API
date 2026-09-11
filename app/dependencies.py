from  app.database import SessionLocal
from app.auth import verify_token
from app.models import User
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    username = payload.get("sub")
    user = db.query(User).filter(User.username == username).first()
    return user
