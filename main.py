from utilities import fonction,token

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


"""GET  REQUESTS"""


@app.get("/incendie/all", tags=["Incendie"])
def get_Incendies():
    """
    Récupères tous les incendies dans une table.
    :return:
    """
    pass

@app.get("/incendie/current", tags=["Incendie"])
def get_Current_Incendies():
    """
    Récupères les incendies
    :return:
    """
    pass

"""POST REQUESTS"""

@app.post("/incendie/new", tags=["Incendie"])
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



@app.post("/capteur/new", tags=["Capteur"])
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
        sql = f"INSERT INTO `Capteur` (nom_capteur, latitude, longtude) VALUES ('{nameCapteur}','{latitude}', '{longitude}')"
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
