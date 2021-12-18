from utilities import fonction, token
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

description = """
API Simulation Projet Scientifique Transverse 🚒

## Projet

Github: <a href="https://github.com/ProjetScientifique">Github ⬜️</a>  
Trello: <a href="https://trello.com/b/U4bDVtQ6/projet-transversal">Trello Projet 📈</a>

## Utilisation API:

Vous devez posseder le token de l'api  


## Token:
### 449928d774153132c2c3509647e3d23f8e168fb50660fa27dd33c8342735b166

"""

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Simulation",
    description=description,
    version="0.0.1",
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["DEBUG"])
def interfaceAPI():
    return {"API Simulation": "Groupe 1"}


"""
.___                                .___.__        
|   | ____   ____  ____   ____    __| _/|__| ____  
|   |/    \_/ ___\/ __ \ /    \  / __ | |  |/ __ \ 
|   |   |  \  \__\  ___/|   |  \/ /_/ | |  \  ___/ 
|___|___|  /\___  >___  >___|  /\____ | |__|\___  >
         \/     \/    \/     \/      \/         \/ 
"""


"""POST REQUESTS"""


@app.post("/incident/", tags=["Incident"], response_model=schemas.Incident)
def nouvel_incident(token_api: str, incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    """
        Adding a new incident dans la base de donnée.</br>
        Les incidents on a besoin de:</br>
            - intensite</br>
            - latitude</br>
            - longitude</br>

        Exemple d'utilisation:
        POST: localhost:8000/new/incident?token="token",detecteur="1",intensite="10",latitude="45.76275055566161",longitude="4.844640087180309"
        <!--
        Python :

        :param token_api: str
        :param detecteur: str
        :param intensite: str
        :param latitude: str
        :param longitude: str
        :return: json response.
        -->
        """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_incidents(db, incident=incident)


"""GET  REQUESTS"""


@app.get("/incident/{incident_id}", tags=["Incident"], response_model=schemas.Incident)
def get_Incident(token_api: str, incident_id: int, db: Session = Depends(get_db)):
    """
    Récupères tous les incidents dans une table.
    :return:
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    db_incident = crud.get_incident(db, incident_id=incident_id)
    if db_incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return db_incident

@app.get("/incidents/", tags=["Incident"], response_model=List[schemas.Incident])
def get_Incidents(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Récupères tous les incidents dans une table.
    :return:
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incidents = crud.get_incidents(db, skip=skip, limit=limit)
    return incidents



"""PATCH REQUESTS"""


@app.patch("/incident/{incident_id}", tags=["Incident"], response_model=schemas.Incident)
def edit_incident(incident_id: int, token_api: str, incident: schemas.IncidentUpdate, db: Session = Depends(get_db)):
    """
        PATCH = met a jour uniquement certaines données
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incident_to_edit = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()
    if incident.id_type_incident: incident_to_edit.id_type_incident = incident.id_type_incident
    if incident.latitude_incident: incident_to_edit.latitude_incident = incident.latitude_incident
    if incident.longitude_incident: incident_to_edit.longitude_incident = incident.longitude_incident
    if incident.intensite_incident: incident_to_edit.intensite_incident = incident.intensite_incident
    if incident.date_incident: incident_to_edit.date_incident = incident.date_incident

    db.commit()
    return incident_to_edit



"""PUT REQUESTS"""


@app.put("/incident/{incident_id}", tags=["Incident"], response_model=schemas.Incident)
def change_incident(incident_id: int,incident:schemas.IncidentCreate, token_api: str, db: Session = Depends(get_db)):
    """
        PUT = réécrit
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incident_to_edit = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()
    incident_to_edit.latitude_incident = incident.latitude_incident
    incident_to_edit.longitude_incident = incident.longitude_incident
    incident_to_edit.intensite_incident = incident.intensite_incident
    incident_to_edit.date_incident = incident.date_incident

    db.commit()

    return incident_to_edit

"""DELETE REQUESTS"""
@app.delete("/incident/{incident_id}", tags=["Incident"], response_model=schemas.Incident)
def delete_incident(incident_id: int, token_api: str, db: Session = Depends(get_db)):
    """
        PUT = réécrit

        """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incident_delete = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()

    if incident_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(incident_delete)
    db.commit()

    return incident_delete


"""
_________                __                       
\_   ___ \_____  _______/  |_  ____  __ _________ 
/    \  \/\__  \ \____ \   __\/ __ \|  |  \_  __ \
\     \____/ __ \|  |_> >  | \  ___/|  |  /|  | \/
 \______  (____  /   __/|__|  \___  >____/ |__|   
        \/     \/|__|             \/              
"""

"""
POST Request
    - Good à tester.
"""


@app.post("/detecteur/", tags=["Detecteur"], response_model=schemas.Detecteur)
def nouveau_Detecteur(detecteur: schemas.DetecteurCreate,token_api: str, db: Session = Depends(get_db)):
    """
    Creer un nouveau detecteur dans la base de donnée.</br>
    Pour cerer un detecteur :</br>
        - NameDetecteur Optionnel</br>
        - latitude</br>
        - longitude</br>

    Exemple d'utilisation:
    POST: localhost:8000/new/detecteur?token="token",nameDetecteur="DetecteurIncroyable",latitude="45.76275055566161",longitude="4.844640087180309"
    <!--
    Python :

    :param detecteur: Json du detecteur à creer
    :param token_api: Token pour acceder à l'API
    :return: json du detecteur créé
    -->
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_detecteur(db, detecteur=detecteur)


"""GET Detecteur"""


@app.get("/detecteur/{id_detecteur}", tags=["Detecteur"], response_model=schemas.Detecteur)
def recuperer_Detecteur(id_detecteur: str, token_api: str, db: Session = Depends(get_db)):
    """
    Creer un nouveau detecteur dans la base de donnée.</br>
    Pour cerer un detecteur :</br>
        - NameDetecteur Optionnel</br>
        - latitude</br>
        - longitude</br>

    Exemple d'utilisation:
    POST: localhost:8000/new/detecteur?token="token",nameDetecteur="DetecteurIncroyable",latitude="45.76275055566161",longitude="4.844640087180309"
    <!--
    Python :

    :param token_api: str
    :param nameDetecteur: str
    :param latitude: str
    :param longitude: str
    :return: json response.
    -->
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    db_detecteur = crud.get_detecteur(db, id_detecteur=id_detecteur)
    if db_detecteur is None:
        raise HTTPException(status_code=404, detail="Detecteur not found")
    return db_detecteur


@app.get("/detecteurs/", tags=["Detecteur"], response_model=List[schemas.Detecteur])
def recuperer_les_Detecteurs(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Creer un nouveau detecteur dans la base de donnée.</br>
    Pour cerer un detecteur :</br>
        - NameDetecteur Optionnel</br>
        - latitude</br>
        - longitude</br>

    Exemple d'utilisation:
    POST: localhost:8000/new/detecteur?token="token",nameDetecteur="DetecteurIncroyable",latitude="45.76275055566161",longitude="4.844640087180309"
    <!--
    Python :

    :param token_api: str
    :param nameDetecteur: str
    :param latitude: str
    :param longitude: str
    :return: json response.
    -->
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    detecteurs = crud.get_detecteurs(db, skip=skip, limit=limit)
    return detecteurs



"""PATCH REQUESTS"""


@app.patch("/detecteur/{detecteurs_id}", tags=["Detecteur"], response_model=schemas.Detecteur)
def edit_detecteur(detecteur_id: int, token_api: str, detecteur: schemas.DetecteurUpdate, db: Session = Depends(get_db)):
    """
    PATCH = met a jour uniquement certaines données


    :param detecteur_id: id du detecteur a modifié
    :param token_api: Token pour acceder à l'API
    :param detecteur: JSON des éléments a modifier
    :return: Json du Detecteur modifié
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    detecteur_to_edit = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()
    if detecteur.id_type_detecteur: detecteur_to_edit.id_type_detecteur = detecteur.id_type_detecteur
    if detecteur.latitude_detecteur: detecteur_to_edit.latitude_detecteur = detecteur.latitude_detecteur
    if detecteur.longitude_detecteur: detecteur_to_edit.longitude_detecteur = detecteur.longitude_detecteur
    if detecteur.nom_detecteur: detecteur_to_edit.nom_detecteur = detecteur.nom_detecteur
    db.commit()
    return detecteur_to_edit



"""PUT REQUESTS"""


@app.put("/detecteur/{detecteurs_id}", tags=["Detecteur"], response_model=schemas.Detecteur)
def change_detecteur(detecteur_id: int,detecteur:schemas.DetecteurCreate, token_api: str, db: Session = Depends(get_db)):
    """
    PUT = réécrit
    Réécrir la totalité du detecteur possédant l'id.

    <!--
    :param detecteur_id: id du detecteur (bdd)
    :param detecteur: json du detecteur modifié
    :param token_api: Token pour acceder à l'api
    :return: json du detecteur modifié
    -->
    """

    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    detecteur_to_edit = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()
    detecteur_to_edit.id_type_detecteur = detecteur.id_type_detecteur
    detecteur_to_edit.latitude_detecteur = detecteur.latitude_detecteur
    detecteur_to_edit.longitude_detecteur = detecteur.longitude_detecteur
    detecteur_to_edit.nom_detecteur = detecteur.nom_detecteur
    db.commit()

    return detecteur_to_edit

"""DELETE REQUESTS"""


@app.delete("/detecteur/{detecteurs_id}", tags=["Detecteur"], response_model=schemas.Detecteur)
def delete_detecteur(detecteur_id: int, token_api: str, db: Session = Depends(get_db)):
    """
    DELETE Detecteur by id.

    :param detecteur_id:
    :param token_api:
    :param db:
    :return:
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    detecteur_delete = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()

    if detecteur_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(detecteur_delete)
    db.commit()

    return detecteur_delete


