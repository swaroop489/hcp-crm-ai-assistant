from pydantic import BaseModel
from typing import Dict, Any, Optional

class ChatRequest(BaseModel):
    message: str
    hcp_id: Optional[int] = None

class ChatResponse(BaseModel):
    response: str
    updated_state: Optional[Dict[str, Any]] = None
