from utilities import fonction,token
from utilities.database import Database

from typing import Optional
from fastapi import FastAPI,HTTPException

description = """
API Simulation Projet Scientifique Transverse 🚒

## Projet

Github: <a href="https://github.com/ProjetScientifique">Github ⬜️</a>  
Trello: <a href="https://trello.com/b/U4bDVtQ6/projet-transversal">Trello Projet 📈</a>

## Utilisation API:

Vous devez posseder le token de l'api  

"""

app = FastAPI(
    title="API Simulation",
    description=description,
    version="0.0.1",
)


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
@app.get("/incendie", tags=["Incendie"])
def get_Incendie(token_recu:str):
    """
    Récupères tous les incendies dans une table.
    :return:
    """
    pass

"""POST REQUESTS"""
@app.post("/incendie", tags=["Incendie"])
def nouvel_incendie(token_recu:str,capteur:str, intensite: str, latitude: str,
                    longitude: str):
    """
    Adding a new incendie dans la base de donnée.</br>
    Les incendies on a besoin de:</br>
        - capteur</br>
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
    if fonction.isCapteur(capteur) and fonction.isIntensite(intensite) and fonction.isLatitude(
            latitude) and fonction.isLongitude(longitude):
        db = "simulation"
        sql = f"INSERT INTO `Incendie` (id_incendie, latitude, longtude, date_incendie, intensite_incendie) VALUES (NULL,'{latitude}', '{longitude}', NOW(), '{intensite}')"
        # Database(db).insert(sql)
        return {"success": {
            "type" : "insert",
            "database" : db,
            "requete" : sql,
            "elements" : {
                "value":{
                    "latitude":latitude,
                    "longitude":longitude,
                    "date_incendie":"now",
                    "intensite_incendie":intensite
                }
            }
        }}

    raise HTTPException(status_code=400, detail="Mauvais format de donnée envoyé, en cas de doute consulter la documentation https://localhost:8000/docs")


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
@app.post("/capteur", tags=["Capteur"])
def nouveau_Capteur(token_recu:str,latitude: str,longitude: str,nameCapteur:Optional[str]="NULL"):
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
    if not token.token(token_recu):raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    if fonction.isLatitude(latitude) and fonction.isLongitude(longitude):
        db = "Simulation"
        sql = f"INSERT INTO `Capteur` (id_capteur, nom_capteur, latitude, longtude) VALUES ('{nameCapteur}','{latitude}', '{longitude}')"
        # Database(db).insert(sql)
        return {"success": {
            "type" : "insert",
            "database" : db,
            "requete" : sql,
            "elements" : {
                "value":{
                    "nom_capteur":nameCapteur,
                    "latitude":latitude,
                    "longitude":longitude
                }
            }
        }}

    raise HTTPException(status_code=400, detail="Mauvais format de donnée envoyé, en cas de doute consulter la documentation https://localhost:8000/docs")

"""GET Capteur"""
@app.get("/capteur", tags=["Capteur"])
def recuperer_Capteur(token_recu:str,idCapteur: str):
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
    if not token.token(token_recu):raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    if fonction.isCapteur(idCapteur):
        db = "Simulation"
        sql = f"SELECT `nom_capteur`, `latitude`, `longtude` FROM `Capteur` WHERE `idCapteur` = '{idCapteur}';"
        Database(db).select(sql)
        return {"success": {
            "type" : "select",
            "database" : db,
            "requete" : sql,
            "elements" : {
                "value":{
                    "nom_capteur":nameCapteur,
                    "latitude":latitude,
                    "longitude":longitude
                }
            }
        }}

    raise HTTPException(status_code=400, detail="Mauvais format de donnée envoyé, en cas de doute consulter la documentation https://localhost:8000/docs")

"""GET Capteur"""
@app.get("/capteurs", tags=["Capteur"])
def recuperer_les_Capteur(token_recu:str):
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
    if not token.token(token_recu):raise HTTPException(status_code=401, detail="Token API non ou mal définit.")

    db = "Simulation"
    sql = f"SELECT nom_capteur, latitude, longtude FROM `Capteur` (nom_capteur, latitude, longtude) VALUES ('{nameCapteur}','{latitude}', '{longitude}')"
    # Database(db).insert(sql)
    return {"success": {
        "type" : "insert",
        "database" : db,
        "requete" : sql,
        "elements" : {
            "value":{
                "nom_capteur":nameCapteur,
                "latitude":latitude,
                "longitude":longitude
            }
        }
    }}