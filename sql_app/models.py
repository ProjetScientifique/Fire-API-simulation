from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Numeric
from sqlalchemy.orm import relationship

from .database import Base


class Incendie(Base):
    __tablename__ = "incendie"
    id_incendie = Column(Integer, primary_key=True)
    date_incendie = Column(TIMESTAMP)
    latitude_incendie = Column(Numeric(precision=9, scale=7))
    longitude_incendie = Column(Numeric(precision=10, scale=7))
    intensite_incendie = Column(Numeric(precision=4, scale=2))

class Capteur(Base):
    __tablename__ = "capteur"
    id_capteur = Column(Integer, primary_key=True)
    nom_capteur = Column(String)
    latitude_capteur = Column(Numeric(precision=9, scale=7))
    longitude_capteur = Column(Numeric(precision=10, scale=7))
