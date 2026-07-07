from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    username : str
    email :  str   
    password : str      

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int
    username : str
    email : str     

class FavoriteCreate(BaseModel):
    job_id : str 
    job_title : str   
    company : str        


class FavoriteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int   
    user_id : int   
    job_id: str
    job_title : str
    company : str

