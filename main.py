from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.dialects.postgresql import UUID
import uuid
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/scholarway")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class EtablissementDB(Base):
    __tablename__ = "etablissements"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom = Column(String, nullable=False)
    type = Column(String)
    localisation = Column(String)
    site_web = Column(String)

app = FastAPI(title="ScholarWay Backend - Full Version")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/recherche")
def rechercher_ecole(ville: str = None, db: Session = Depends(get_db)):
    """Recherche réelle dans PostgreSQL"""
    query = db.query(EtablissementDB)
    if ville:
        query = query.filter(EtablissementDB.localisation.ilike(f"%{ville}%"))
    return query.all()

@app.get("/orientation/matching")
def lancer_matching(moyenne: float, serie: str, budget: float):
    """Ton algorithme de matching intelligent"""
    recommandations = []
    serie = serie.upper()
    
    if serie in ["C", "D"] and moyenne >= 14:
        if budget >= 500000:
            recommandations.append({"ecole": "EPL", "filiere": "Génie Logiciel", "score": 0.98})
    elif serie in ["G2", "G3"] and moyenne >= 12:
        recommandations.append({"ecole": "IUT", "filiere": "Gestion", "score": 0.85})
    
    return {"suggestions": recommandations}