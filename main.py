from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import psycopg2  # Nécessaire pour la base de données

# 1. Initialisation
app = FastAPI(title="ScholarWay Backend")

# 2. Modèles complets (Source: Diagramme de Classes)
class Etablissement(BaseModel):
    nom: str
    type: str  # Universite, Ecole, Institut
    localisation: str
    description: str
    contact: str
    siteWeb: str

class Bachelier(BaseModel):
    nom: str
    prenom: str           # Ajouté
    email: str            # Ajouté
    telephone: str        # Ajouté
    serieBac: str
    moyenneBac: float
    budgetMax: float      # Ajouté pour le matching

# 3. Simulation de données (En attendant PostgreSQL via Docker)
db_universites = [
    {
        "id": 1,
        "nom": "Université de Lomé",
        "type": "Université",
        "localisation": "Lomé",
        "siteWeb": "https://www.univ-lome.tg"
    }
]

# 4. Routes (Source: Cas d'Utilisation)

@app.get("/")
def home():
    return {"message": "Bienvenue sur ScholarWay"}

@app.get("/recherche")
def rechercher_etablissement(nom: Optional[str] = None):
    if nom:
        resultats = [e for e in db_universites if nom.lower() in e["nom"].lower()]
        return {"resultats": resultats}
    return {"resultats": db_universites}

@app.get("/chatbot")
def chatbot_ia(question: str):
    # Implémente genererReponse()
    return {"reponse": f"Analyse de : '{question}'. Je suis l'assistant ScholarWay."}

@app.get("/orientation/matching")
def lancer_matching(moyenne: float, serie: str, budget: float):
    # Implémente calculerScore() avec budget
    score = 0.0
    if serie.upper() == "C" and moyenne >= 14 and budget >= 500000:
        score = 0.95
        recommandation = "Génie Logiciel (EPL)"
    else:
        score = 0.70
        recommandation = "Informatique de Gestion"
    
    return {"recommandation": recommandation, "score_pertinence": score}