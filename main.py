import re,json
from typing import Optional
from fastapi import FastAPI
from database import Database


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.put("/new/incendie")
def nouvel_incendie(capteur: Optional[str],intensite: Optional[str],latitude: Optional[str],longitude: Optional[str]):
    """
    Adding a new incendie dans la base de donnée.
    Les incendies on :


    :param capteur: str
    :param intensite: str
    :return: json response.
    """

    if capteur and intensite and latitude and longitude:
        return {"success","true"}
    # with a match in case capteur =! souhaité.
    # intensité != int.
    sql = ""
    #Database.insert(sql)
    return {"erreur":"a"}
