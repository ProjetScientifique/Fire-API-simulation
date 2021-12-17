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


@app.post("/incendie/", tags=["Incendie"], response_model=schemas.Incendie)
def nouvel_incendie(token_recu: str, incendie: schemas.IncendieCreate, db: Session = Depends(get_db)):
    """
        Adding a new incendie dans la base de donnée.</br>
        Les incendies on a besoin de:</br>
            - intensite</br>
            - latitude</br>
            - longitude</br>

        Exemple d'utilisation:
        POST: localhost:8000/new/incendie?token="token",capteur="1",intensite="10",latitude="45.76275055566161",longitude="4.844640087180309"
        <!--
        Python :

        :param token_recu: str
        :param capteur: str
        :param intensite: str
        :param latitude: str
        :param longitude: str
        :return: json response.
        -->
        """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_incendies(db, incendie=incendie)


"""GET  REQUESTS"""


@app.get("/incendie/{incendie_id}", tags=["Incendie"], response_model=schemas.Incendie)
def get_Incendie(token_recu: str, incendie_id: int, db: Session = Depends(get_db)):
    """
    Récupères tous les incendies dans une table.
    :return:
    """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    db_incendie = crud.get_incendie(db, incendie_id=incendie_id)
    if db_incendie is None:
        raise HTTPException(status_code=404, detail="Incendie not found")
    return db_incendie

@app.get("/incendies/", tags=["Incendie"], response_model=List[schemas.Incendie])
def get_Incendies(token_recu: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Récupères tous les incendies dans une table.
    :return:
    """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incendies = crud.get_incendies(db, skip=skip, limit=limit)
    return incendies



"""PATCH REQUESTS"""


@app.patch("/incendie/{incendie_id}", tags=["Incendie"], response_model=schemas.Incendie)
def edit_incendie(incendie_id: int, token_recu: str, incendie: schemas.IncendieUpdate, db: Session = Depends(get_db)):
    """
        PATCH = met a jour uniquement certaines données
    """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incendie_to_edit = db.query(models.Incendie).filter(models.Incendie.id_incendie == incendie_id).first()
    if incendie.latitude_incendie: incendie_to_edit.latitude_incendie = incendie.latitude_incendie
    if incendie.longitude_incendie: incendie_to_edit.longitude_incendie = incendie.longitude_incendie
    if incendie.intensite_incendie: incendie_to_edit.intensite_incendie = incendie.intensite_incendie
    if incendie.date_incendie: incendie_to_edit.date_incendie = incendie.date_incendie

    db.commit()
    return incendie_to_edit



"""PUT REQUESTS"""


@app.put("/incendie/{incendie_id}", tags=["Incendie"], response_model=schemas.Incendie)
def change_incendie(incendie_id: int,incendie:schemas.IncendieCreate, token_recu: str, db: Session = Depends(get_db)):
    """
        PUT = réécrit
    """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incendie_to_edit = db.query(models.Incendie).filter(models.Incendie.id_incendie == incendie_id).first()
    incendie_to_edit.latitude_incendie = incendie.latitude_incendie
    incendie_to_edit.longitude_incendie = incendie.longitude_incendie
    incendie_to_edit.intensite_incendie = incendie.intensite_incendie
    incendie_to_edit.date_incendie = incendie.date_incendie

    db.commit()

    return incendie_to_edit

"""DELETE REQUESTS"""
@app.delete("/incendie/{incendie_id}", tags=["Incendie"], response_model=schemas.Incendie)
def delete_incendie(incendie_id: int, token_recu: str, db: Session = Depends(get_db)):
    """
        PUT = réécrit

        """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incendie_delete = db.query(models.Incendie).filter(models.Incendie.id_incendie == incendie_id).first()

    if incendie_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(incendie_delete)
    db.commit()

    return incendie_delete


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


@app.post("/capteur/", tags=["Capteur"], response_model=schemas.Capteur)
def nouveau_Capteur(capteur: schemas.CapteurCreate,token_recu: str, db: Session = Depends(get_db)):
    """
    Creer un nouveau capteur dans la base de donnée.</br>
    Pour cerer un capteur :</br>
        - NameCapteur Optionnel</br>
        - latitude</br>
        - longitude</br>

    Exemple d'utilisation:
    POST: localhost:8000/new/capteur?token="token",nameCapteur="CapteurIncroyable",latitude="45.76275055566161",longitude="4.844640087180309"
    <!--
    Python :

    :param capteur: Json du capteur à creer
    :param token_recu: Token pour acceder à l'API
    :return: json du capteur créé
    -->
    """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_capteur(db, capteur=capteur)


"""GET Capteur"""


@app.get("/capteur/{id_capteur}", tags=["Capteur"], response_model=schemas.Capteur)
def recuperer_Capteur(id_capteur: str, token_recu: str, db: Session = Depends(get_db)):
    """
    Creer un nouveau capteur dans la base de donnée.</br>
    Pour cerer un capteur :</br>
        - NameCapteur Optionnel</br>
        - latitude</br>
        - longitude</br>

    Exemple d'utilisation:
    POST: localhost:8000/new/capteur?token="token",nameCapteur="CapteurIncroyable",latitude="45.76275055566161",longitude="4.844640087180309"
    <!--
    Python :

    :param token_recu: str
    :param nameCapteur: str
    :param latitude: str
    :param longitude: str
    :return: json response.
    -->
    """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    db_capteur = crud.get_capteur(db, id_capteur=id_capteur)
    if db_capteur is None:
        raise HTTPException(status_code=404, detail="Capteur not found")
    return db_capteur


@app.get("/capteurs/", tags=["Capteur"], response_model=List[schemas.Capteur])
def recuperer_les_Capteurs(token_recu: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Creer un nouveau capteur dans la base de donnée.</br>
    Pour cerer un capteur :</br>
        - NameCapteur Optionnel</br>
        - latitude</br>
        - longitude</br>

    Exemple d'utilisation:
    POST: localhost:8000/new/capteur?token="token",nameCapteur="CapteurIncroyable",latitude="45.76275055566161",longitude="4.844640087180309"
    <!--
    Python :

    :param token_recu: str
    :param nameCapteur: str
    :param latitude: str
    :param longitude: str
    :return: json response.
    -->
    """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    capteurs = crud.get_capteurs(db, skip=skip, limit=limit)
    return capteurs



"""PATCH REQUESTS"""


@app.patch("/capteur/{capteurs_id}", tags=["Capteur"], response_model=schemas.Capteur)
def edit_capteur(capteur_id: int, token_recu: str, capteur: schemas.CapteurUpdate, db: Session = Depends(get_db)):
    """
    PATCH = met a jour uniquement certaines données


    :param capteur_id: id du capteur a modifié
    :param token_recu: Token pour acceder à l'API
    :param capteur: JSON des éléments a modifier
    :return: Json du Capteur modifié
    """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    capteur_to_edit = db.query(models.Capteur).filter(models.Capteur.id_capteur == capteur_id).first()
    if capteur.latitude_capteur: capteur_to_edit.latitude_capteur = capteur.latitude_capteur
    if capteur.longitude_capteur: capteur_to_edit.longitude_capteur = capteur.longitude_capteur
    if capteur.nom_capteur: capteur_to_edit.nom_capteur = capteur.nom_capteur
    db.commit()
    return capteur_to_edit



"""PUT REQUESTS"""


@app.put("/capteur/{capteurs_id}", tags=["Capteur"], response_model=schemas.Capteur)
def change_capteur(capteur_id: int,capteur:schemas.CapteurCreate, token_recu: str, db: Session = Depends(get_db)):
    """
    PUT = réécrit
    Réécrir la totalité du capteur possédant l'id.

    <!--
    :param capteur_id: id du capteur (bdd)
    :param capteur: json du capteur modifié
    :param token_recu: Token pour acceder à l'api
    :return: json du capteur modifié
    -->
    """

    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    capteur_to_edit = db.query(models.Capteur).filter(models.Capteur.id_capteur == capteur_id).first()
    capteur_to_edit.latitude_capteur = capteur.latitude_capteur
    capteur_to_edit.longitude_capteur = capteur.longitude_capteur
    capteur_to_edit.nom_capteur = capteur.nom_capteur
    db.commit()

    return capteur_to_edit

"""DELETE REQUESTS"""


@app.delete("/capteur/{capteurs_id}", tags=["Capteur"], response_model=schemas.Capteur)
def delete_capteur(capteur_id: int, token_recu: str, db: Session = Depends(get_db)):
    """
    DELETE Capteur by id.

    :param capteur_id:
    :param token_recu:
    :param db:
    :return:
    """
    if not token.token(token_recu): raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    capteur_delete = db.query(models.Capteur).filter(models.Capteur.id_capteur == capteur_id).first()

    if capteur_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(capteur_delete)
    db.commit()

    return capteur_delete


