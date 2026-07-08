from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database import crud
from app.schemas.interaction import Interaction as InteractionSchema
from app.schemas.response import APIResponse
from typing import List

router = APIRouter()

@router.get("/{interaction_id}", response_model=APIResponse)
def get_interaction(interaction_id: int, db: Session = Depends(get_db)):
    interaction = crud.get_interaction(db, interaction_id)
    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return APIResponse(data=interaction)
