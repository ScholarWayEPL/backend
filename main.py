from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

app = FastAPI(title="ScholarWay Backend - Version Finale")

class Filiere(BaseModel):
    id_filiere: int
    id_etablissement: int
    nom_filiere: str
    description: str
    debouches: str
    coefficient_base: float
    moyenne_min: float

class Etablissement(BaseModel):
    id_etablissement: int
    nom: str
    type: str 
    localisation: str 
    description: str
    contact: str
    siteWeb: str

class Bachelier(BaseModel):
    nom: str
    prenom: str
    email: EmailStr
    telephone: str
    serieBac: str
    moyenneBac: float = Field(..., ge=0, le=20)
    budgetMax: float


db_etablissements = [
    {"id": 1, "nom": "EPL (Polytechnique)", "type": "Ecole", "localisation": "Lomé (Adidogomé)", "contact": "2221...", "siteWeb": "epl.univ-lome.tg"},
    {"id": 2, "nom": "ENSI", "type": "Ecole", "localisation": "Lomé", "contact": "2225...", "siteWeb": "ensi.tg"},
    {"id": 3, "nom": "UK (Université de Kara)", "type": "Université", "localisation": "Kara", "contact": "2330...", "siteWeb": "univ-kara.tg"}
]

db_bacheliers = [] 

@app.post("/inscription", status_code=status.HTTP_201_CREATED)
def inscrire_bachelier(bachelier: Bachelier):
    """Permet à un bachelier de s'enregistrer (Table bacheliers du SQL)"""
    db_bacheliers.append(bachelier.dict())
    return {"message": f"Bachelier {bachelier.nom} inscrit avec succès", "total": len(db_bacheliers)}

@app.get("/recherche", response_model=List[dict])
def rechercher_etablissement(nom: Optional[str] = None, ville: Optional[str] = None):
    """Filtrage par ville (Lomé, Kara, etc.) selon le diagramme"""
    resultats = db_etablissements
    if nom:
        resultats = [e for e in resultats if nom.lower() in e["nom"].lower()]
    if ville:
        resultats = [e for e in resultats if ville.lower() in e["localisation"].lower()]
    return resultats

@app.get("/orientation/matching")
def lancer_matching(moyenne: float, serie: str, budget: float):
    """Algorithme de calcul du score de pertinence"""
    if moyenne < 0 or moyenne > 20:
        raise HTTPException(status_code=400, detail="La moyenne doit être comprise entre 0 et 20")
    
    recommandations = []
    serie = serie.upper()

    
    if serie in ["C", "D", "E"] and moyenne >= 14:
        if budget >= 500000:
            recommandations.append({"ecole": "EPL", "filiere": "Génie Logiciel", "score": 0.98})
        recommandations.append({"ecole": "ENSI", "filiere": "Génie Électrique", "score": 0.85})
    
    elif serie in ["G2", "G3"] and moyenne >= 12:
        recommandations.append({"ecole": "IUT Gestion", "filiere": "Comptabilité", "score": 0.80})
    
    else:
        recommandations.append({"ecole": "FDS Lomé", "filiere": "Tronc Commun", "score": 0.70})

    return {
        "bachelier_stats": {"moyenne": moyenne, "serie": serie, "budget": budget},
        "suggestions": recommandations
    }