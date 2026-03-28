"""
APPLICATION CONFIGURATION FILE

INSTRUCTIONS:
1. Load environment variables from .env
2. Create a config class
3. Define database connection string
"""

# TODO: import os
import os

# TODO: load .env file
from dotenv import load_dotenv
load_dotenv()

# TODO: create Config class
# Example:
# DB_URI = "mysql+pymysql://user:password@localhost/db_name"
class Config:
    DB_USER = os.environ.get("DB_USER")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_NAME = os.environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
