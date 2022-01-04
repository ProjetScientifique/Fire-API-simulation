from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Numeric
from sqlalchemy.orm import relationship

from .database import Base


class Type_incident(Base):
    __tablename__ = "type_incident"
    id_type_incident = Column(Integer, primary_key=True)
    nom_type_incident = Column(String)

    incidents = relationship("Incident", back_populates="type_incident")


class Incident(Base):
    __tablename__ = "incident"
    id_incident = Column(Integer, primary_key=True)
    id_type_incident = Column(Integer, ForeignKey('type_incident.id_type_incident'))
    date_incident = Column(TIMESTAMP)
    latitude_incident = Column(Numeric(precision=9, scale=7))
    longitude_incident = Column(Numeric(precision=10, scale=7))
    intensite_incident = Column(Numeric(precision=4, scale=2))

    type_incident = relationship("Type_incident", back_populates="incidents")

class Type_detecteur(Base):
    __tablename__ = "type_detecteur"
    id_type_detecteur = Column(Integer, primary_key=True)
    nom_type_detecteur = Column(String)

    detecteur = relationship("Detecteur", back_populates="type")


class Detecteur(Base):
    __tablename__ = "detecteur"
    id_detecteur = Column(Integer, primary_key=True)
    id_type_detecteur = Column(Integer, ForeignKey('type_detecteur.id_type_detecteur'))
    nom_detecteur = Column(String)
    latitude_detecteur = Column(Numeric(precision=9, scale=7))
    longitude_detecteur = Column(Numeric(precision=10, scale=7))

    type = relationship("Type_detecteur", back_populates="detecteur")
