from sqlalchemy import create_engine #creates the connection between app and the sql database
from sqlalchemy.ext.declarative import declarative_base #allows sqlalchemy to translate python to SQL query and SQL query to python data
from sqlalchemy.orm import sessionmaker 
from config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
