from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum

class StatusEnum(str, enum.Enum):
    approved = "approved"
    rejected = "rejected"

class SentimentEnum(str, enum.Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.approved)
    sentiment = Column(Enum(SentimentEnum), default=SentimentEnum.neutral)
