import os
from pydantic import BaseSettings
#  pydantic makes data validation and settings management very simple for users and developers.
#  It allows us as developers to define strict typing parameters for our request/response objects, 
# and also provides extremely friendly error messages to users who violate those parameters.
class Settings(BaseSettings):
    PROJECT_NAME: str = 'Job Tracker'
    PROJECT_VERSION: str = '1.0.0'
    SQLALCHEMY_DATABASE_URL: str = os.environ.get('SQLALCHEMY_DATABASE_URL') #connection to DB
    class Config:
        env_file = '.env'

settings = Settings()
