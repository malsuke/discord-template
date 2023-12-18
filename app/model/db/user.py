from sqlalchemy import Column, String, DateTime, BigInteger
from sqlalchemy.orm import relationship
from datetime import datetime
from model.db.db_config import Base


class UserModel(Base):
    __tablename__ = "users"
    user_discord_id: int = Column(BigInteger, primary_key=True)
    user_name: String = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime)
    points = relationship("PointModel", back_populates="user")
