CREATE SCHEMA IF NOT EXISTS strava;

CREATE TABLE IF NOT EXISTS strava.sport (
    id UUID PRIMARY KEY,
    id_salarie INT,
    nom TEXT,
    prenom TEXT,
    type_sport TEXT,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    duration_minutes INT,
    distance_m INT
);

#
#DataWarehouse
#

CREATE SCHEMA IF NOT EXISTS dwh;

#
#Dimenssions
#

CREATE TABLE dwh.dim_salarie (
    id_salarie     INT PRIMARY KEY,
    nom            TEXT,
    prenom         TEXT,
    salaire_brut   NUMERIC,
    moyen_de_deplacement TEXT
);


CREATE TABLE dwh.dim_sport (
    id_sport SERIAL PRIMARY KEY,
    type_sport TEXT UNIQUE
);



CREATE TABLE dwh.dim_date (
    date_id DATE PRIMARY KEY,
    jour INT,
    mois INT,
    annee INT,
    semaine INT,
    jour_semaine TEXT
);

INSERT INTO dwh.dim_date (
    date_id,
    jour,
    mois,
    annee,
    semaine,
    jour_semaine
)
SELECT
    d::date,
    EXTRACT(DAY FROM d),
    EXTRACT(MONTH FROM d),
    EXTRACT(YEAR FROM d),
    EXTRACT(WEEK FROM d),
    TO_CHAR(d, 'Day')
FROM generate_series('2024-01-01', '2034-01-01', interval '1 day') d;


#
#Fait
#

CREATE TABLE dwh.fact_sport_activity (
    id UUID PRIMARY KEY,

    id_salarie INT REFERENCES dwh.dim_salarie(id_salarie),
    id_sport INT REFERENCES dwh.dim_sport(id_sport),
    date_id DATE REFERENCES dwh.dim_date(date_id),

    duration_minutes INT,
    distance_m INT
);
