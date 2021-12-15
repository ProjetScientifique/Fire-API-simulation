from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP,NUMERIC
from sqlalchemy.orm import relationship

from .database import Base

class Incendie(Base):
    __tablename__ = "incendie"
    id_incendie = Column(Integer,primary_key=True,)
    date_incendie = Column(TIMESTAMP)
    latitude_incendie = Column(NUMERIC(precision=7, scale=9))
    longitude_incendie = Column(NUMERIC(precision=7 , scale=10))
    intensite_incendie = Column(NUMERIC(precision=2 , scale=4))


class Capteur(Base):
    __tablename__ = "capteur"
    id_capteur = Column(Integer,primary_key=True,)
    nom_capteur = Column(String)
    latitude_capteur = Column(NUMERIC(precision=7, scale=9))
    longitude_capteur = Column(NUMERIC(precision=7 , scale=10))


class Detecte(Base):
    __tablename__ = "detecte"
    id_capteur = Column(Integer, ForeignKey("capteur.id_capteur"))
    id_incendie = Column(Integer, ForeignKey("incendie.id_capteur"))
    intensite_detecte = Column(NUMERIC(precision=2 , scale=4))
