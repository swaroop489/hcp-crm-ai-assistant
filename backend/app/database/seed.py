from app.database.database import SessionLocal, engine, Base
from app.database.models import HCP
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    if db.query(HCP).count() == 0:
        logger.info("Seeding HCP database...")
        doctors = [
            HCP(name="Dr. Smith", specialization="Cardiology", hospital="City General"),
            HCP(name="Dr. Jane Doe", specialization="Oncology", hospital="Mercy Hospital"),
            HCP(name="Dr. John", specialization="Neurology", hospital="St. Judes")
        ]
        db.add_all(doctors)
        db.commit()
        logger.info("Seeding completed.")
    else:
        logger.info("Database already seeded.")
    
    db.close()

if __name__ == "__main__":
    seed_db()
