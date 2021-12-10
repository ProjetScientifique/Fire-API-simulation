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


@app.get("/")
def interfaceAPI():
    return {"API Simulation": "Groupe 1"}


@app.post("/new/incendie")
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

    :param token: str
    :param capteur: str
    :param intensite: str
    :param latitude: str
    :param longitude: str
    :return: json response.
    -->
    """
    if not token.token(token_recu):     raise HTTPException(status_code=401, detail="Token API non ou mal définit.")
    if fonction.isCapteur(capteur) and fonction.isIntensite(intensite) and fonction.isLatitude(
            latitude) and fonction.isLongitude(longitude):
        db = "incendie"
        sql = f"INSERT INTO table (id_incendie, latitude, longtude, date_incendie, intensite_incendie) VALUES (NULL,'{latitude}', '{longitude}', NOW(), '{intensite}')"
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
