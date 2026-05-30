import pandas as pd

import random
import uuid
from datetime import datetime, timedelta
import json
import time


# -----------------------------
# Load & clean data
# -----------------------------
df = pd.read_csv("RH_Sport.csv")


# -----------------------------
# Vitesses cohérentes par sport (km/h)
# -----------------------------
Vitesse_par_type = {
    "Runing": (6, 10),     
    "Randonnée": (3, 5),   
    "Natation": (1, 4),   
    "Voile": (8, 20),      
    "Triathlon": (10, 18),  # Vitesse moyenne globale (mix course/vélo/natation)
}

Sport_avec_distance= set(Vitesse_par_type.keys())


# -----------------------------
# Generator
# -----------------------------

row = df.sample(n=1).iloc[0]

id_salarie=row["id_salarie"]
Nom=row["nom"]
Prenom= row["prenom"]
type_sport=row["type_sport"]


start_time = datetime.now() - timedelta(days=random.randint(0, 365))

if start_time.weekday()>=5:
    # Heures  week-end
    hour = random.choice(list(range(6, 21)))  
else:
    # Heures hors travail
    hour = random.choice([6, 7, 18, 19, 20])

start_time = start_time.replace(hour=hour, minute=random.randint(0, 59))

duration_minutes = random.randint(10, 180)
end_time = start_time + timedelta(minutes=duration_minutes)

# Distance
if type_sport in Sport_avec_distance:
    min_speed, max_speed = Vitesse_par_type[type_sport]
    speed_kmh = random.uniform(min_speed, max_speed)
    distance_m = int(speed_kmh * (duration_minutes / 60) * 1000)
else:
    distance_m = None

event= {
    "id": str(uuid.uuid4()),
    "id_salarie": int(id_salarie),
    "Nom": Nom,
    "Prenom": Prenom,
    "type_sport": type_sport,
    "start_time": start_time.isoformat(),
    "end_time": end_time.isoformat(),
    "duration_minutes": int(duration_minutes),
    "distance_m": distance_m
}


with open('output.json', 'w') as f:
    json.dump(event, f)





