from sqlalchemy.orm import Session
from . import models, schemas


def get_incendie(db: Session, incendie_id: int):
    return db.query(models.Incendie).filter(models.Incendie.id_incendie == incendie_id).first()


def get_incendies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Incendie).offset(skip).limit(limit).all()


def create_incendies(db: Session, incendie: schemas.IncendieCreate):
    db_incendie = models.Incendie(latitude_incendie=incendie.latitude_incendie,
                                  longitude_incendie=incendie.longitude_incendie,
                                  intensite_incendie=incendie.intensite_incendie, date_incendie=incendie.date_incendie)
    db.add(db_incendie)
    db.commit()
    db.refresh(db_incendie)
    return db_incendie



def get_capteur(db: Session, id_capteur: int):
    return db.query(models.Capteur).filter(models.Capteur.id_capteur == id_capteur).first()


def get_capteurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Capteur).offset(skip).limit(limit).all()


def create_capteur(db: Session, capteur: schemas.CapteurCreate):
    db_capteur = models.Capteur(latitude_capteur=capteur.latitude_capteur, longitude_capteur=capteur.longitude_capteur,
                                nom_capteur=capteur.nom_capteur)
    db.add(db_capteur)
    db.commit()
    db.refresh(db_capteur)
    return db_capteur
