from utilities import fonction,token
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



# 449928d774153132c2c3509647e3d23f8e168fb50660fa27dd33c8342735b166

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

"""GET  REQUESTS"""
@app.get("/incendie/{incendie_id}", tags=["Incendie"], response_model=schemas.Incendie)
def get_Incendie(token_recu:str,incendie_id: int, db: Session = Depends(get_db)):
    """
    Récupères tous les incendies dans une table.
    :return:
    """
    if not token.token(token_recu):raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    db_incendie = crud.get_incendie(db, incendie_id=incendie_id)
    if db_incendie is None:
        raise HTTPException(status_code=404, detail="Incendie not found")
    return db_incendie

"""GET  REQUESTS"""
@app.get("/incendies/", tags=["Incendie"], response_model=List[schemas.Incendie])
def get_Incendies(token_recu:str,skip:int=0, limit:int=100, db: Session = Depends(get_db)):
    """
    Récupères tous les incendies dans une table.
    :return:
    """
    if not token.token(token_recu):raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    incendies = crud.get_incendies(db, skip=skip, limit=limit)
    return incendies


"""POST REQUESTS"""
@app.post("/incendie/", tags=["Incendie"], response_model=schemas.Incendie)
def nouvel_incendie(token_recu:str, incendie: schemas.IncendieCreate, db: Session = Depends(get_db)):
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
    if not token.token(token_recu):raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.create_incendies(db,incendie=incendie)

"""PATCH REQUESTS"""
@app.patch("/incendie/{incendie_id}", tags=["Incendie"], response_model=schemas.Incendie)
def edit_incendie(incendie_id: int,token_recu:str, incendie: schemas.IncendieCreate, db: Session = Depends(get_db)):
    """
        PATCH = met a jour uniquement certaines données

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
    if not token.token(token_recu):raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    return crud.recreate_incendies(db,incendie=incendie)

"""PUT REQUESTS"""
@app.put("/incendie/{incendie_id}", tags=["Incendie"], response_model=schemas.Incendie)
def change_incendie(incendie_id: int,token_recu: str, incendie: schemas.IncendieCreate, db: Session = Depends(get_db)):
    """
        PUT = réécrit

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
def nouveau_Capteur(token_recu:str,capteur: schemas.CapteurCreate, db:Session=Depends(get_db)):
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
    return crud.create_capteur(db, capteur=capteur)

"""GET Capteur"""
@app.get("/capteur/{id_capteur}", tags=["Capteur"], response_model=schemas.Capteur)
def recuperer_Capteur(token_recu:str,id_capteur: str, db: Session = Depends(get_db)):
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
def recuperer_les_Capteurs(token_recu:str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
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
