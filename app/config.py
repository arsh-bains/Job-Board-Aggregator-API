from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # your four fields here
    DATABASE_URL:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int


    model_config = SettingsConfigDict(env_file=".env")