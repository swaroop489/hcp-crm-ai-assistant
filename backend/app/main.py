from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import api_router
from app.database.database import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HCP CRM AI Assistant API",
    description="Backend API for AI-first CRM HCP Module",
    version="1.0.0"
)

# Enable CORS for the frontend (Vite default port 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all API routes
app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the HCP CRM AI Assistant API"}
