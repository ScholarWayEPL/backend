from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from uuid import UUID, uuid4
app = FastAPI(title="ScholarWay Backend - Version UUID")


class Filiere(BaseModel):
    id_filiere: UUID = Field(default_factory=uuid4)
    id_etablissement: UUID
    nom_filiere: str
    coefficient_base: float
    moyenne_min: float

class Etablissement(BaseModel):
    id_etablissement: UUID = Field(default_factory=uuid4)
    nom: str
    type: str 
    localisation: str 
    siteWeb: str

class Bachelier(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    nom: str
    prenom: str
    email: EmailStr
    serieBac: str
    moyenneBac: float = Field(..., ge=0, le=20)
    budgetMax: float

db_etablissements = [
    {"id": uuid4(), "nom": "EPL (Polytechnique)", "type": "Ecole", "localisation": "Lomé (Adidogomé)"},
    {"id": uuid4(), "nom": "ENSI", "type": "Ecole", "localisation": "Lomé"}
]

@app.post("/inscription", status_code=status.HTTP_201_CREATED)
def inscrire_bachelier(bachelier: Bachelier):
    return {"message": "Inscrit avec UUID", "uid": bachelier.id}

@app.get("/orientation/matching")
def lancer_matching(moyenne: float, serie: str, budget: float):
    return {"status": "Matching OK", "moyenne": moyenne}