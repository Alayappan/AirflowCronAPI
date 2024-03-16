from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PG_USER:str
    PG_PASSWORD:str
    PG_DATABASE:str
    PG_HOST:str
    PG_PORT:int
    PG_TABLE:str


    class Config:
        env_file = ".env"

settings = Settings()