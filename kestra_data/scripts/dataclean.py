import pandas as pd


# -----------------------------
# Load & join 
# -----------------------------
df1 = pd.read_csv("Sport.csv")
df2 = pd.read_csv("RH.csv")


df1.columns = ["id_salarie", "type_sport"]


to_drop = ['Date de naissance', "Date d'embauche", 'Type de contrat']
df2 = df2.drop(columns=to_drop)

df2.columns=['id_salarie', 'nom', 'prenom', 'bu_equipe', 'salaire_brut',
       'nombre_cp', 'adresse', 'moyen_de_deplacement']


df = df2.merge(df1, on="id_salarie", how="left")


# Nettoyage
df["type_sport"] = df["type_sport"].str.strip()
df = df[df["type_sport"].notna() & (df["type_sport"] != "")]


df['moyen_de_deplacement'] = df['moyen_de_deplacement'].replace({
    'véhicule thermique/électrique': 'auto_moto',
    'Vélo/Trottinette/Autres': 'velo_trot',
    'Transports en commun': 'transport',
    'Marche/running': 'a_pied'
})



# -----------------------------
# Calcul distance
# -----------------------------


import openrouteservice

client = openrouteservice.Client(
    key= os.getenv("KEY_API_GEO")) 
)

def geocode(adresse):

    result = client.pelias_search(adresse)

    coords = result['features'][0]['geometry']['coordinates']

    return coords

def distance_km(adresse1, adresse2):

    coord1 = geocode(adresse1)
    coord2 = geocode(adresse2)

    route = client.directions(
        [coord1, coord2],
        profile='driving-car'
    )

    distance_m = route['routes'][0]['summary']['distance']

    return round(distance_m / 1000, 2)


adresse_entreprise="1362 Av. des Platanes, 34970 Lattes"


distances = []

for adresse_domicile in df['adresse']:
    distance = distance_km(
        adresse_domicile,
        adresse_entreprise
    )
    distances.append(distance)




df['distance_domicile_travail'] = distances

df.to_csv("RH_Sport.csv", index=False)




