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
        re.search("^\d$",capteur)
        re.search("^[1-9][0-9]?$|^100$",intensite)
        re.search("^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)$",latitude)#match latitude
        re.search("^[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$",longitude)#match latitude
        sql = ""
        # Database.insert(sql)
        return {"success","true"}


    return {"erreur":"a"}
