from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def getSessionLocal(settings):

    SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.PG_USER}:{settings.PG_PASSWORD}@{settings.PG_HOST}:{settings.PG_PORT}/{settings.PG_DATABASE}"

    print(SQLALCHEMY_DATABASE_URL)
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


    return SessionLocal, engine