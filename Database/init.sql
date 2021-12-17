DROP TABLE IF EXISTS incendie;
DROP TABLE IF EXISTS capteur;
DROP TABLE IF EXISTS detecte;

CREATE TABLE incendie (
    id_incendie SERIAL NOT NULL,
    date_incendie TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    latitude_incendie NUMERIC(9,7),
    longitude_incendie NUMERIC(10,7),
    intensite_incendie NUMERIC(4,2),
    CONSTRAINT pk_id_incendie PRIMARY KEY (id_incendie)
);

CREATE TABLE capteur (
    id_capteur SERIAL NOT NULL,
    nom_capteur VARCHAR(255),
    latitude_capteur NUMERIC(9,7),
    longitude_capteur NUMERIC(10,7),
    CONSTRAINT pk_id_capteur PRIMARY KEY (id_capteur)
);

CREATE TABLE detecte (
    id_incendie SERIAL NOT NULL,
    id_capteur SERIAL NOT NULL,
    intensite_detecte NUMERIC(4,2),
    CONSTRAINT pk_id_capteur_id_incendie PRIMARY KEY (id_capteur, id_incendie)
);

ALTER TABLE detecte
    ADD CONSTRAINT fk_detecte_id_incendie FOREIGN KEY (id_incendie) REFERENCES incendie(id_incendie);

ALTER TABLE detecte
    ADD CONSTRAINT fk_detecte_id_capteur FOREIGN KEY (id_capteur) REFERENCES capteur(id_capteur);
