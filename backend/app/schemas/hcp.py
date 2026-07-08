from pydantic import BaseModel
from typing import Optional

class HCPBase(BaseModel):
    name: str
    specialization: Optional[str] = None
    contact_info: Optional[str] = None
    hospital: Optional[str] = None

class HCPCreate(HCPBase):
    pass

class HCP(HCPBase):
    id: int

    class Config:
        from_attributes = True
