from pydantic import BaseModel
from typing import Optional
from datetime import date, time
from app.database.models import SentimentEnum

class InteractionBase(BaseModel):
    hcp_id: int
    interaction_type: Optional[str] = None
    date: Optional[date] = None
    time: Optional[time] = None
    topics_discussed: Optional[str] = None
    materials_shared: Optional[str] = None
    samples_distributed: Optional[str] = None
    sentiment: Optional[SentimentEnum] = None
    outcomes: Optional[str] = None
    follow_up_actions: Optional[str] = None

class InteractionCreate(InteractionBase):
    pass

class InteractionUpdate(BaseModel):
    interaction_type: Optional[str] = None
    date: Optional[date] = None
    time: Optional[time] = None
    topics_discussed: Optional[str] = None
    materials_shared: Optional[str] = None
    samples_distributed: Optional[str] = None
    sentiment: Optional[SentimentEnum] = None
    outcomes: Optional[str] = None
    follow_up_actions: Optional[str] = None

class Interaction(InteractionBase):
    id: int

    class Config:
        from_attributes = True
