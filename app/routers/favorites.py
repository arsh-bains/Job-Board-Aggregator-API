from fastapi import Depends,APIRouter
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import verify_token
from app.database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    username = payload.get("sub")
    user = db.query(models.User).filter(models.User.username == username).first()
    return user

@router.post("/favorites")
def save_favorite(
    favorite: schemas.FavoriteCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_fav = models.Favorite(job_id=favorite.job_id, job_title=favorite.job_title, 
                              company=favorite.company, user_id=current_user.id) 
    db.add(new_fav)
    db.commit()
    db.refresh(new_fav)
    return new_fav

@router.get("/favorites")
def get_favs(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(models.Favorite).filter(models.Favorite.user_id == current_user.id).all()

@router.delete("/favorites/{job_id}")
def del_favs(job_id: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    fav = db.query(models.Favorite).filter(models.Favorite.user_id == current_user.id,
    models.Favorite.job_id == job_id).first()
    db.delete(fav)
    db.commit()
    return {"message": "Deleted"}
