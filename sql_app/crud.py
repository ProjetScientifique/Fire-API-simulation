from sqlalchemy.orm import Session
from . import models, schemas


def get_incendie(db: Session, incendie_id: int):
    return db.query(models.Incendie).filter(models.Incendie.id == incendie_id).first()


def get_incendies(db: Session):
    return db.query(models.Incendie)


def create_incendies(db: Session, incendie: schemas.IncendieCreate):
    db_incendie = models.Incendie(incendie_latitude=incendie.latitude, incendie_longitude=incendie.longitude)
    db.add(db_incendie)
    db.commit()
    db.refresh(db_incendie)
    return db_incendie
