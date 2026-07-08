from sqlalchemy.orm import Session
from app.database.models import HCP, Interaction
from app.schemas.hcp import HCPCreate
from app.schemas.interaction import InteractionCreate
from app.core.constants import SentimentEnum

def get_hcps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(HCP).offset(skip).limit(limit).all()

def search_hcp_by_name(db: Session, query: str):
    return db.query(HCP).filter(HCP.name.ilike(f"%{query}%")).all()

def create_hcp(db: Session, hcp: HCPCreate):
    db_hcp = HCP(**hcp.dict())
    db.add(db_hcp)
    db.commit()
    db.refresh(db_hcp)
    return db_hcp

def create_interaction(db: Session, interaction: dict):
    db_interaction = Interaction(**interaction)
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

def get_interaction(db: Session, interaction_id: int):
    return db.query(Interaction).filter(Interaction.id == interaction_id).first()

def update_interaction(db: Session, interaction_id: int, updates: dict):
    db_interaction = get_interaction(db, interaction_id)
    if db_interaction:
        for key, value in updates.items():
            setattr(db_interaction, key, value)
        db.commit()
        db.refresh(db_interaction)
    return db_interaction
