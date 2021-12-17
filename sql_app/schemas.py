from typing import List, Optional
from pydantic import BaseModel
import datetime

class IncidentBase(BaseModel):
    id_type_incident: int
    latitude_incident: float
    longitude_incident: float
    intensite_incident: float
    date_incident: datetime.datetime


class IncidentUpdate(BaseModel):
    id_type_incident: Optional[int]
    latitude_incident: Optional[float]
    longitude_incident: Optional[float]
    intensite_incident: Optional[float]
    date_incident: Optional[datetime.datetime]


class IncidentCreate(IncidentBase):
    pass


class Incident(IncidentBase):
    id_incident: int

    class Config:
        orm_mode = True
        """schema_extra = {
            'A_EDIT': {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }"""


class DetecteurBase(BaseModel):
    latitude_detecteur: float
    longitude_detecteur: float
    nom_detecteur: str

class DetecteurUpdate(BaseModel):
    latitude_detecteur: Optional[float]
    longitude_detecteur: Optional[float]
    nom_detecteur: Optional[str]


class DetecteurCreate(DetecteurBase):
    pass


class Detecteur(DetecteurBase):
    id_detecteur: int

    class Config:
        orm_mode = True
