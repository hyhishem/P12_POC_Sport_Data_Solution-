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

CREATE SCHEMA IF NOT EXISTS BI;

CREATE TABLE IF NOT EXISTS BI.prime_sport (
    id_salarie          INT PRIMARY KEY,
    nom                 TEXT,
    prenom              TEXT,
    nb_activites        INT,
    moyen_de_deplacement TEXT,    
    salaire_brut        NUMERIC,
    prime               NUMERIC,
    eligible_avantage_prime      BOOLEAN,
    eligible_avantage_5jours       BOOLEAN
);
