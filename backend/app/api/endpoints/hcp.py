from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import HCP
from app.schemas.hcp import HCP as HCPSchema, HCPCreate
from typing import List

router = APIRouter()

@router.get("/", response_model=List[HCPSchema])
def get_hcps(db: Session = Depends(get_db)):
    """
    Get all Healthcare Professionals to populate the dropdown in the UI.
    """
    hcps = db.query(HCP).all()
    return hcps

@router.post("/", response_model=HCPSchema)
def create_hcp(hcp: HCPCreate, db: Session = Depends(get_db)):
    """
    Create a new HCP.
    """
    db_hcp = HCP(**hcp.dict())
    db.add(db_hcp)
    db.commit()
    db.refresh(db_hcp)
    return db_hcp
