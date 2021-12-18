from sqlalchemy.orm import Session
from . import models, schemas


def get_incident(db: Session, incident_id: int):
    return db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()


def get_incidents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Incident).offset(skip).limit(limit).all()


def create_incidents(db: Session, incident: schemas.IncidentCreate):
    db_incident = models.Incident(id_type_incident=incident.id_type_incident,
                                  latitude_incident=incident.latitude_incident,
                                  longitude_incident=incident.longitude_incident,
                                  intensite_incident=incident.intensite_incident, date_incident=incident.date_incident)
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


def get_detecteur(db: Session, id_detecteur: int):
    return db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == id_detecteur).first()


def get_detecteurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Detecteur).offset(skip).limit(limit).all()


def create_detecteur(db: Session, detecteur: schemas.DetecteurCreate):
    db_detecteur = models.Detecteur(id_type_detecteur=detecteur.id_type_detecteur,
                                    latitude_detecteur=detecteur.latitude_detecteur,
                                    longitude_detecteur=detecteur.longitude_detecteur,
                                    nom_detecteur=detecteur.nom_detecteur)
    db.add(db_detecteur)
    db.commit()
    db.refresh(db_detecteur)
    return db_detecteur
