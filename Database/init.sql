DROP TABLE IF EXISTS incident;
DROP TABLE IF EXISTS detecteur;
DROP TABLE IF EXISTS detecte;
DROP TABLE IF EXISTS type_incident;
DROP TABLE IF EXISTS type_detecteur;

CREATE TABLE incident (
    id_incident SERIAL NOT NULL,
    id_type_incident SERIAL NOT NULL,
    date_incident TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    latitude_incident NUMERIC(9,7),
    longitude_incident NUMERIC(10,7),
    intensite_incident NUMERIC(4,2),
    CONSTRAINT pk_id_incident PRIMARY KEY (id_incident)
);

CREATE TABLE detecteur (
    id_detecteur SERIAL NOT NULL,
    id_type_detecteur SERIAL NOT NULL,
    nom_detecteur VARCHAR(255),
    latitude_detecteur NUMERIC(9,7),
    longitude_detecteur NUMERIC(10,7),
    CONSTRAINT pk_id_detecteur PRIMARY KEY (id_detecteur)
);

CREATE TABLE detecte (
    id_incident SERIAL NOT NULL,
    id_detecteur SERIAL NOT NULL,
    intensite_detecte NUMERIC(4,2),
    CONSTRAINT pk_id_detecteur_id_incident PRIMARY KEY (id_detecteur, id_incident)
);

CREATE TABLE type_detecteur (
    id_type_detecteur SERIAL NOT NULL,
    nom_type_detecteur VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_type_detecteur PRIMARY KEY (id_type_detecteur)
);

CREATE TABLE type_incident (
    id_type_incident SERIAL NOT NULL,
    nom_type_incident VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_type_incident PRIMARY KEY (id_type_incident)
);

ALTER TABLE detecte
    ADD CONSTRAINT fk_detecte_id_incident FOREIGN KEY (id_incident) REFERENCES incident(id_incident);

ALTER TABLE detecte
    ADD CONSTRAINT fk_detecte_id_detecteur FOREIGN KEY (id_detecteur) REFERENCES detecteur(id_detecteur);

ALTER TABLE detecteur
    ADD CONSTRAINT fk_detecteur_id_type_detecteur FOREIGN KEY (id_type_detecteur) REFERENCES type_detecteur(id_type_detecteur);

ALTER TABLE incident
    ADD CONSTRAINT fk_incident_id_type_incident FOREIGN KEY (id_type_incident) REFERENCES type_incident(id_type_incident);

INSERT INTO type_detecteur (nom_type_detecteur) VALUES ('Detecteur');
INSERT INTO type_incident (nom_type_incident) VALUES ('Incident');
