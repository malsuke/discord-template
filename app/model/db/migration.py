from sqlalchemy import create_engine, Column, Integer, DateTime, ForeignKey, BigInteger, String
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv as ld

env_path = os.path.join(os.path.dirname(__file__), "../../.env")
ld(env_path)

MYSQL_USER = os.environ["MYSQL_USER"]
MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
MYSQL_HOST = os.environ["MYSQL_HOST"]
MYSQL_DATABASE = os.environ["MYSQL_DATABASE"]

engine = create_engine(f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DATABASE}")
Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"
    user_discord_id: int = Column(BigInteger, primary_key=True)
    user_name: String = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime)
    points = relationship("PointModel", back_populates="user")


class PointModel(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    point = Column(BigInteger, default=0, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime)
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="points")
    user_id = Column(BigInteger, ForeignKey("users.user_discord_id"))


Base.metadata.create_all(engine)
