from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

MYSQL_USER = os.environ["MYSQL_USER"]
MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
MYSQL_HOST = os.environ["MYSQL_HOST"]
MYSQL_DATABASE = os.environ["MYSQL_DATABASE"]

engine = create_engine(f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DATABASE}")
Base = declarative_base()

Base.metadata.create_all(engine)
