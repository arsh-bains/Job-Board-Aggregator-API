from fastapi import Depends,APIRouter, HTTPException,status
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_current_user,get_db


router = APIRouter()


@router.post("/favorites", response_model=schemas.FavoriteOut)
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

@router.get("/favorites", response_model=list[schemas.FavoriteOut])
def get_favs(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(models.Favorite).filter(models.Favorite.user_id == current_user.id).all()

@router.delete("/favorites/{job_id}")
def del_favs(job_id: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    fav = db.query(models.Favorite).filter(models.Favorite.user_id == current_user.id,
    models.Favorite.job_id == job_id).first()
    if fav is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    db.delete(fav)
    db.commit()
    return {"message": "Deleted"}
