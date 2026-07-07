from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # your four fields here
    DATABASE_URL:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int


    class Config:
        env_file = ".env"

