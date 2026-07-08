from sqlalchemy import Column, Integer, String, Date, Time, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from .database import Base

class SentimentEnum(str, enum.Enum):
    POSITIVE = "Positive"
    NEUTRAL = "Neutral"
    NEGATIVE = "Negative"

class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    specialization = Column(String(255))
    contact_info = Column(String(255))
    hospital = Column(String(255))

    interactions = relationship("Interaction", back_populates="hcp")

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_id = Column(Integer, ForeignKey("hcps.id"))
    interaction_type = Column(String(100))
    date = Column(Date)
    time = Column(Time)
    topics_discussed = Column(Text)
    materials_shared = Column(Text)
    samples_distributed = Column(Text)
    sentiment = Column(Enum(SentimentEnum))
    outcomes = Column(Text)
    follow_up_actions = Column(Text)

    hcp = relationship("HCP", back_populates="interactions")
