from typing import List, Optional
from pydantic import BaseModel
import datetime

class IncendieBase(BaseModel):
    latitude_incendie: float
    longitude_incendie: float
    intensite_incendie: float
    date_incendie: datetime.datetime


class IncendieUpdate(BaseModel):
    latitude_incendie: Optional[float]
    longitude_incendie: Optional[float]
    intensite_incendie: Optional[float]
    date_incendie: Optional[datetime.datetime]


class IncendieCreate(IncendieBase):
    pass


class Incendie(IncendieBase):
    id_incendie: int

    class Config:
        orm_mode = True


class CapteurBase(BaseModel):
    latitude_capteur: float
    longitude_capteur: float
    nom_capteur: str

class CapteurUpdate(BaseModel):
    latitude_capteur: Optional[float]
    longitude_capteur: Optional[float]
    nom_capteur: Optional[str]


class CapteurCreate(CapteurBase):
    pass


class Capteur(CapteurBase):
    id_capteur: int

    class Config:
        orm_mode = True
