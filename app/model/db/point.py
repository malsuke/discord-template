from sqlalchemy import Column, Integer, DateTime, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime
from model.db.db_config import Base
from model.db.user import UserModel


class PointModel(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    point = Column(BigInteger, default=0, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime)
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="points")
    user_id = Column(BigInteger, ForeignKey("users.user_discord_id"))
