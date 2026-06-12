import pandas as pd
from sqlalchemy import create_engine,text
import os


df = pd.read_csv("RH_Sport.csv")

# Transformations
df["nb_activites"] = 0
df["prime"] = df["salaire_brut"] * 0.05
df["eligible_avantage_prime"] = df["moyen_de_deplacement"].isin(
    ["velo_trot", "a_pied"]
)
df["eligible_avantage_5jours"] = False

# Garder uniquement les colonnes de la table cible
df = df[
    [
        "id_salarie",
        "nom",
        "prenom",
        "nb_activites",
        "moyen_de_deplacement",
        "salaire_brut",
        "prime",
        "eligible_avantage_prime",
        "eligible_avantage_5jours",
    ]
]



# Connexion PostgreSQL
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@postgres:5432/{os.getenv('POSTGRES_DB')}"
)

 

with engine.begin() as conn:
    conn.exec_driver_sql("TRUNCATE TABLE bi.prime_sport")    
    
    
# Insertion
df.to_sql(
    "prime_sport",
    con=engine,
    schema="bi",
    if_exists="append",
    index=False,
    method="multi"
)




