from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    # your columns here
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    favorites = relationship("Favorite", back_populates="owner")



class Favorite(Base):
    __tablename__ = "favorites"
    # your columns here
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id") , index=True)
    job_id = Column(String, unique=False, nullable=False)
    job_title =  Column(String, unique=False, nullable=False)
    company = Column(String, unique=False, nullable=False)
    owner = relationship("User", back_populates="favorites")


