from fastapi import APIRouter
from app.api.endpoints import chat, hcp

api_router = APIRouter()
api_router.include_router(chat.router, prefix="/chat", tags=["Chat"])
api_router.include_router(hcp.router, prefix="/hcp", tags=["HCP"])
