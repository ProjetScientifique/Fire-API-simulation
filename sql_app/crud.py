from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

# get un incident
def get_incident(db: Session, incident_id: int):
    return db.query(models.Incident). \
        filter(models.Incident.id_incident == incident_id). \
        first()

# get tous les incidents
def get_incidents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Incident).offset(skip).limit(limit).all()

# create un incident
def create_incident(db: Session, incident: schemas.IncidentCreate):
    db_incident = models.Incident(id_type_incident=incident.id_type_incident,
                                  latitude_incident=incident.latitude_incident,
                                  longitude_incident=incident.longitude_incident,
                                  intensite_incident=incident.intensite_incident,
                                  date_incident=incident.date_incident)
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

# patch un incident
def patch_incident(db: Session, incident: schemas.IncidentUpdate, incident_id: int):
    incident_to_edit = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()
    if incident.id_type_incident: incident_to_edit.id_type_incident = incident.id_type_incident
    if incident.latitude_incident: incident_to_edit.latitude_incident = incident.latitude_incident
    if incident.longitude_incident: incident_to_edit.longitude_incident = incident.longitude_incident
    if incident.intensite_incident: incident_to_edit.intensite_incident = incident.intensite_incident
    if incident.date_incident: incident_to_edit.date_incident = incident.date_incident

    db.commit()
    return incident_to_edit
# put un incident
def put_incident(db: Session, incident: schemas.IncidentUpdate, incident_id: int):
    incident_to_edit = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()
    incident_to_edit.latitude_incident = incident.latitude_incident
    incident_to_edit.longitude_incident = incident.longitude_incident
    incident_to_edit.intensite_incident = incident.intensite_incident
    incident_to_edit.date_incident = incident.date_incident

    db.commit()
    return incident_to_edit


# delete un incident
def delete_incident(db: Session, incident_id: int):
    incident_delete = db.query(models.Incident).filter(models.Incident.id_incident == incident_id).first()

    if incident_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(incident_delete)
    db.commit()

    return incident_delete

# get un detecteur
def get_detecteur(db: Session, id_detecteur: int):
    return db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == id_detecteur).first()

# get tous les detecteurs
def get_detecteurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Detecteur).offset(skip).limit(limit).all()

# create un detecteur
def create_detecteur(db: Session, detecteur: schemas.DetecteurCreate):
    db_detecteur = models.Detecteur(id_type_detecteur=detecteur.id_type_detecteur,
                                    latitude_detecteur=detecteur.latitude_detecteur,
                                    longitude_detecteur=detecteur.longitude_detecteur,
                                    nom_detecteur=detecteur.nom_detecteur)
    db.add(db_detecteur)
    db.commit()
    db.refresh(db_detecteur)
    return db_detecteur


# patch un detecteur
def patch_detecteur(db: Session, detecteur: schemas.DetecteurUpdate, detecteur_id: int):
    
    detecteur_to_patch = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()
    
    if detecteur.id_type_detecteur: detecteur_to_patch.id_type_detecteur = detecteur.id_type_detecteur
    if detecteur.latitude_detecteur: detecteur_to_patch.latitude_detecteur = detecteur.latitude_detecteur
    if detecteur.longitude_detecteur: detecteur_to_patch.longitude_detecteur = detecteur.longitude_detecteur
    
    db.commit()
    return detecteur_to_patch

# put un detecteur
def put_detecteur(db: Session, detecteur: schemas.DetecteurUpdate, detecteur_id: int):
    
    detecteur_to_put = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()
    detecteur_to_put.id_type_detecteur = detecteur.id_type_detecteur
    detecteur_to_put.latitude_detecteur = detecteur.latitude_detecteur
    detecteur_to_put.longitude_detecteur = detecteur.longitude_detecteur

    db.commit()
    return detecteur_to_put

# delete un detecteur
def delete_detecteur(db: Session, detecteur_id: int):
    detecteur_to_delete = db.query(models.Detecteur).filter(models.Detecteur.id_detecteur == detecteur_id).first()

    if detecteur_to_delete is None:
        raise HTTPException(status_code=404, detail="Resource Not Found")

    db.delete(detecteur_to_delete)
    db.commit()
    return detecteur_to_delete

# get les types d'incident par id
def get_type_incident_by_id(db: Session, id_type_incident: int):
    return db.query(models.Type_incident).filter(models.Type_incident.id_type_incident == id_type_incident).first()

# get les types d'incident par le nom
def get_type_incident_by_nom(db: Session, nom_type_incident: str):
    return db.query(models.Type_incident).filter(models.Type_incident.nom_type_incident == nom_type_incident).first()

# get tous les types d'incident
def get_types_incidents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Type_incident).offset(skip).limit(limit).all()

# get un type de detecteur par l'id
def get_type_detecteur_by_id(db: Session, id_type_detecteur: int):
    return db.query(models.Type_detecteur).filter(models.Type_detecteur.id_type_detecteur == id_type_detecteur).first()

# get un type de detecteur par son nom
def get_type_detecteur_by_nom(db: Session, nom_type_detecteur: str):
    return db.query(models.Type_detecteur).filter(
        models.Type_detecteur.nom_type_detecteur == nom_type_detecteur).first()

# get tous les detecteurs
def get_types_detecteurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Type_detecteur).offset(skip).limit(limit).all()

# create une detection (moment ou le capteur detecte un feu)
def create_detecte_event(db: Session, detecte: schemas.Detecte):
    db_detect = models.Detecte(id_incident=detecte.id_incident,
                               id_detecteur=detecte.id_detecteur,
                               date_detecte=detecte.date_detecte,
                               intensite_detecte=detecte.intensite_detecte
                               )
    db.add(db_detect)
    db.commit()
    db.refresh(db_detect)
    return db_detect

# get une detection (moment ou le capteur detecte un feu)
def get_detecte_event(id_incident:int , id_detecteur:int ,db: Session):
    return db.query(models.Detecte).\
        filter(models.Detecte.id_detecteur == id_detecteur).\
        filter(models.Detecte.id_incident == id_incident).\
        first()

# get toutes les detections (moment ou le capteur detecte un feu)
def get_detectes_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Detecte).offset(skip).limit(limit).all()
