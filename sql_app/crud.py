from sqlalchemy.orm import Session
from . import models, schemas


def get_incendie(db: Session, incendie_id: int):
    return db.query(models.Incendie).filter(models.Incendie.id_incendie == incendie_id).first()


def get_incendies(db: Session):
    return db.query(models.Incendie)


def create_incendies(db: Session, incendie: schemas.IncendieCreate):
    db_incendie = models.Incendie(incendie_latitude=incendie.latitude_incendie, incendie_longitude=incendie.longitude_incendie)
    db.add(db_incendie)
    db.commit()
    db.refresh(db_incendie)
    return db_incendie


def get_capteurs(db: Session):
    return db.query(models.Capteur)


def get_capteur(db: Session, id_capteur: int):
    return db.query(models.Capteur).filter(models.Capteur.id_capteur == id_capteur)


def create_capteur(db: Session, capteur: schemas.CapteurCreate):
    db_capteur = models.Capteur(capteur_latitude=capteur.latitude_capteur, capteur_longitude=capteur.longitude_capteur,
                                name_capteur=capteur.nom_capteur)
    db.add(db_capteur)
    db.commit()
    db.refresh(db_capteur)
    return db_capteur
