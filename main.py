from utilities import fonction, token
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

description = """
API Simulation Projet Scientifique Transverse π

## Projet

Github: <a href="https://github.com/ProjetScientifique">Github π»</a>  
Trello: <a href="https://trello.com/b/U4bDVtQ6/projet-transversal">Trello Projet π</a>

## Utilisation API:

Vous devez posseder le token de l'api  


## Token π :
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
        Adding a new incident dans la base de donnΓ©e.</br>
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
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    return crud.create_incident(db, incident=incident)


"""GET  REQUESTS"""


@app.get("/incident/{incident_id}", tags=["Incident"], response_model=schemas.IncidentAll)
def get_Incident(token_api: str, incident_id: int, db: Session = Depends(get_db)):
    """
    RΓ©cupΓ¨res tous les incidents dans une table.
    :return:
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    db_incident = crud.get_incident(db, incident_id=incident_id)
    if db_incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return db_incident


@app.get("/incidents/", tags=["Incident"], response_model=List[schemas.IncidentAll])
def get_Incidents(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    RΓ©cupΓ¨res tous les incidents dans une table.
    :return:
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    incidents = crud.get_incidents(db, skip=skip, limit=limit)
    return incidents


"""PATCH REQUESTS"""


@app.patch("/incident/{incident_id}", tags=["Incident"], response_model=schemas.Incident)
def edit_incident(incident_id: int, token_api: str, incident: schemas.IncidentUpdate, db: Session = Depends(get_db)):
    """
        PATCH = met a jour uniquement certaines donnΓ©es
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    return crud.patch_incident(db, incident=incident, incident_id = incident_id)


"""PUT REQUESTS"""


@app.put("/incident/{incident_id}", tags=["Incident"], response_model=schemas.Incident)
def change_incident(incident_id: int, incident: schemas.IncidentCreate, token_api: str, db: Session = Depends(get_db)):
    """
        PUT = rΓ©Γ©crit
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    return crud.put_incident(db, incident=incident, incident_id=incident_id)


"""DELETE REQUESTS"""


@app.delete("/incident/{incident_id}", tags=["Incident"], response_model=schemas.Incident)
def delete_incident(incident_id: int, token_api: str, db: Session = Depends(get_db)):
    """
        PUT = rΓ©Γ©crit
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    return crud.delete_incident(db, incident_id = incident_id)


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
    - Good Γ  tester.
"""


@app.post("/detecteur/", tags=["Detecteur"], response_model=schemas.Detecteur)
def nouveau_Detecteur(detecteur: schemas.DetecteurCreate, token_api: str, db: Session = Depends(get_db)):
    """
    Creer un nouveau detecteur dans la base de donnΓ©e.</br>
    Pour cerer un detecteur :</br>
        - NameDetecteur Optionnel</br>
        - latitude</br>
        - longitude</br>

    Exemple d'utilisation:
    POST: localhost:8000/new/detecteur?token="token",nameDetecteur="DetecteurIncroyable",latitude="45.76275055566161",longitude="4.844640087180309"
    <!--
    Python :

    :param detecteur: Json du detecteur Γ  creer
    :param token_api: Token pour acceder Γ  l'API
    :return: json du detecteur crΓ©Γ©
    -->
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    return crud.create_detecteur(db, detecteur=detecteur)


"""GET Detecteur"""


@app.get("/detecteur/{id_detecteur}", tags=["Detecteur"], response_model=schemas.Detecteur)
def recuperer_Detecteur(id_detecteur: str, token_api: str, db: Session = Depends(get_db)):
    """
    Creer un nouveau detecteur dans la base de donnΓ©e.</br>
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
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    db_detecteur = crud.get_detecteur(db, id_detecteur=id_detecteur)
    if db_detecteur is None:
        raise HTTPException(status_code=404, detail="Detecteur not found")
    return db_detecteur


@app.get("/detecteurs/", tags=["Detecteur"], response_model=List[schemas.Detecteur])
def recuperer_les_Detecteurs(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Creer un nouveau detecteur dans la base de donnΓ©e.</br>
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
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    detecteurs = crud.get_detecteurs(db, skip=skip, limit=limit)
    return detecteurs


"""PATCH REQUESTS"""


@app.patch("/detecteur/{detecteurs_id}", tags=["Detecteur"], response_model=schemas.Detecteur)
def edit_detecteur(detecteur_id: int, token_api: str, detecteur: schemas.DetecteurUpdate,
                   db: Session = Depends(get_db)):
    """
    PATCH = met a jour uniquement certaines donnΓ©es


    :param detecteur_id: id du detecteur a modifiΓ©
    :param token_api: Token pour acceder Γ  l'API
    :param detecteur: JSON des Γ©lΓ©ments a modifier
    :return: Json du Detecteur modifiΓ©
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    return crud.patch_detecteur(db, detecteur = detecteur, detecteur_id = detecteur_id)


"""PUT REQUESTS"""


@app.put("/detecteur/{detecteurs_id}", tags=["Detecteur"], response_model=schemas.Detecteur)
def change_detecteur(detecteur_id: int, detecteur: schemas.DetecteurCreate, token_api: str,
                     db: Session = Depends(get_db)):
    """
    PUT = rΓ©Γ©crit
    RΓ©Γ©crir la totalitΓ© du detecteur possΓ©dant l'id.

    <!--
    :param detecteur_id: id du detecteur (bdd)
    :param detecteur: json du detecteur modifiΓ©
    :param token_api: Token pour acceder Γ  l'api
    :return: json du detecteur modifiΓ©
    -->
    """

    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    return crud.put_detecteur(db, detecteur = detecteur, detecteur_id = detecteur_id)


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
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    return crud.delete_detecteur(db, detecteur_id = detecteur_id)



@app.get("/incidents/type/", tags=["type", "Incident"], response_model=List[schemas.Type_incident])
def recuperer_les_type_incidents(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    type_incidents = crud.get_types_incidents(db, skip=skip, limit=limit)
    return type_incidents


@app.get("/incident/type/name/", tags=["type", "Incident"], response_model=schemas.Type_incident)
def recuperer_incident_by_name(token_api: str, name_incident: str, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    type_incidents = crud.get_type_incident_by_nom(db, nom_type_incident=name_incident)
    return type_incidents


@app.get("/incident/type/", tags=["type", "Incident"], response_model=schemas.Type_incident)
def recuperer_incident_by_id(token_api: str, id_incident: int, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    type_incidents = crud.get_type_incident_by_id(db, id_type_incident=id_incident)
    return type_incidents


@app.get("/detecteurs/type/", tags=["type", "Detecteur"], response_model=List[schemas.Type_detecteur])
def recuperer_les_type_detecteurs(token_api: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    type_detecteurs = crud.get_types_detecteurs(db, skip=skip, limit=limit)
    return type_detecteurs


@app.get("/detecteur/type/name/", tags=["type", "Detecteur"], response_model=schemas.Type_detecteur)
def recuperer_detecteur_by_name(token_api: str, name_detecteur: str, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    type_detecteurs = crud.get_type_detecteur_by_nom(db, nom_type_detecteur=name_detecteur)
    return type_detecteurs


@app.get("/detecteur/type/", tags=["type", "Detecteur"], response_model=schemas.Type_detecteur)
def recuperer_detecteur_by_id(token_api: str, id_detecteur: int, db: Session = Depends(get_db)):
    """
    Ne devrait normalement pas servir 
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    type_detecteurs = crud.get_type_detecteur_by_id(db, id_type_detecteur=id_detecteur)
    return type_detecteurs


@app.post("/detecte/", tags=["Detecteur", "Incident", "Detecte"], response_model=schemas.Detecte)
def create_detecte_event(detecte: schemas.Detecte, token_api: str, db: Session = Depends(get_db)):
    """
    {
      "id_detecteur": 3,
      "intensite_detecte": 25,
      "id_incident": 13,
      "date_detecte": "2022-01-04T10:38:12.197000+00:00"
    }

    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    event = crud.create_detecte_event(db, detecte=detecte)
    return event

@app.get("/detecte/", tags=["Detecte"], response_model=schemas.Detecte)
def get_detecte_event(id_detecteur:int, id_incident:int, token_api: str, db: Session = Depends(get_db)):
    """
    {
      "id_detecteur": 3,
      "intensite_detecte": 25,
      "id_incident": 13,
      "date_detecte": "2022-01-04T10:38:12.197000+00:00"
    }

    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    db_detecteur = crud.get_detecte_event(id_incident,id_detecteur,db)
    if db_detecteur is None:
        raise HTTPException(status_code=404, detail="Event Detecte not found")
    return db_detecteur

@app.get("/detectes/", tags=["Detecte"], response_model=List[schemas.Detecte])
def get_detectes_events(token_api: str,skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)):
    """
    {
      "id_detecteur": 3,
      "intensite_detecte": 25,
      "id_incident": 13,
      "date_detecte": "2022-01-04T10:38:12.197000+00:00"
    }

    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    db_detecteur = crud.get_detectes_events(db,skip,limit)
    if db_detecteur is None:
        raise HTTPException(status_code=404, detail="Event Detecte not found")
    return db_detecteur

@app.delete("/detecte/", tags=["Detecte"], response_model=schemas.Detecte)
def delete_detecte(id_incident:int, id_detecteur:int, token_api: str, db: Session = Depends(get_db)):
    """

    :param id_detecteur: int
    :param id_incident: int
    :param token_api: str
    :return: schema.Detecte
    """
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    detecte_event_to_delete = db.query(models.Detecte).\
        filter(models.Detecte.id_detecteur == id_detecteur).\
        filter(models.Detecte.id_incident == id_incident).\
        first()

    if detecte_event_to_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(detecte_event_to_delete)
    db.commit()

    return detecte_event_to_delete



"""
    DELETE ALL 
"""

# Permet de delete tous les Γ©lΓ©ments dans la table incident et detecteur mais Γ©galement de remettre les ids Γ  1
@app.delete("/delete_all/", tags=["RESET"])
def delete_all_element_database(token_api: str, db: Session = Depends(get_db)):
    """
        Supprime toutes les entrΓ©s de toutes les tables.
    """
    
    if not token.token(token_api): raise HTTPException(status_code=401, detail="Token API non ou mal dΓ©finit.")
    
    detectes = get_detectes_events(token_api, 0, 100, db=db)
    for detecte in detectes:
        delete_detecte(detecte.id_incident, detecte.id_detecteur, token_api, db)

    detecteurs = recuperer_les_Detecteurs(token_api, 0, 100, db=db)
    for detecteur in detecteurs:
        delete_detecteur(detecteur.id_detecteur, token_api, db)
        # remise de l'id detecteur Γ  1
        engine.execute('ALTER SEQUENCE public.detecteur_id_detecteur_seq RESTART WITH 1;')

    incidents = get_Incidents(token_api, 0, 100, db=db)
    for incident in incidents:
        delete_incident(incident.id_incident, token_api, db)
        # remise de l'id incident Γ  1
        engine.execute('ALTER SEQUENCE public.incident_id_incident_seq RESTART WITH 1;')

    return {"status":200,"message":"Toutes les Γ©lΓ©ments des tables (incident, detecteur, detecte) sont supprimΓ©es"}
