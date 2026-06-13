# POC Sport Data Solution

## 1. Contexte et détails du projet

## Présentation

Dans le cadre d'un Proof of Concept (POC), Sport Data Solution met en place une plateforme visant à valoriser la pratique sportive des collaborateurs.

L'objectif est d'automatiser la collecte et le traitement des données RH et sportives afin de déterminer l'éligibilité des salariés à différents avantages :

- Une prime annuelle de 5 % du salaire brut pour les collaborateurs utilisant un mode de déplacement sportif pour se rendre au bureau.
- 5 journées « bien-être » supplémentaires pour les salariés ayant une pratique sportive régulière.

Le projet permet également de :

- Centraliser les données RH et sportives.
- Automatiser les traitements et les calculs d'éligibilité.
- Mettre en place une architecture événementielle pour la circulation des données.
- Publier automatiquement les activités sportives sur Slack.
- Alimenter un Data Warehouse pour le suivi des KPI.
- Assurer la qualité des données et le monitoring de la plateforme.


## Objectifs

### Objectifs métier

- Encourager la pratique sportive en entreprise.
- Identifier les salariés éligibles aux avantages sportifs.
- Mesurer l’impact financier du dispositif.
- Favoriser l’engagement via les publications Slack.

### Objectifs techniques

- Construire un pipeline de données automatisé de bout en bout.
- Mettre en place une architecture événementielle (PostgreSQL, Debezium, Redpanda).
- Alimenter un Data Warehouse pour le reporting (Metabase).
- Garantir la qualité et la cohérence des données.
- Mettre en place un système de monitoring complet.

### Technologies utilisées
- Docker pour la conteneurisation
- Docker Compose pour l'orchestration locale des conteneurs
- Git pour le versioning
- Python pour les scripts d'ingestion et de transformation
- Kestra pour l'orchestration des workflows
- PostgreSQL pour le stockage des données
- Redpanda comme broker de messages  des événements sportifs
- Slack API pour les notifications automatiques
- Metabase comme outil BI
- Prometheus pour la collecte des métriques
- Grafana pour le monitoring et la supervision

## 2. Prérequis
Avant de pouvoir utiliser ce projet, assurez-vous d'avoir installé les éléments suivants :

- **Docker** et **Docker Compose** : pour déployer les conteneurs. 
  - [Installer Docker](https://docs.docker.com/desktop/) 
  - [Installer Docker Compose](https://docs.docker.com/compose/install/)

- **Git** :
  - [Installer Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)
 
Après avoir installé Git, placez-vous dans le dossier où vous souhaitez cloner le dépôt distant, puis exécutez la commande suivante :

 ```bash
git clone https://github.com/hyhishem/P12_POC_Sport_Data_Solution-.git
 ```
Ensuite, accédez au dossier cloné :

 ```bash
cd P12_POC_Sport_Data_Solution-
 ```


## 3. Variable d'environement et secret Kestra

Renommer le fichier et completer les variables d'environements

 ```bash
.env.exemple -> .env
 ```


 ```bash
  while read -r line; do
      key="${line%%=*}"
      value="${line#*=}"
      echo "SECRET_${key}=$(printf '%s' "$value" | base64 -w 0)"
  done < .env > .env_encoded
 ```





## 4. Docker image 

Construire l'image utilisée par les workflows Kestra :

```bash
docker build -t python-strava-pandas:latest -f Dockerfile .
```

Vérifier que l'image a bien été créée :

```bash
docker images
```

## 5. Démarrage de la plateforme

Lancer l'ensemble des services :

```bash
docker compose up -d
```

Vérifier que tous les conteneurs sont actifs :

```bash
docker ps
```
## 6. Démarrage de la plateforme

Une fois les services démarrés, connectez-vous à Kestra :

```bash
http://localhost:8080
```

Importez ensuite les fichiers YAML présents dans les sous dossiers de  /data_kestra/Workflows 

## 7. Ordre d'exécution des workflows

Après avoir importé les workflows dans Kestra, exécuter les workflows dans l'ordre suivant :

### 1. Nettoyage et enrichissement des données RH

**Workflow :** `projet12_datacleaning`

Ce workflow nettoie les données RH et calcule la distance domicile-travail afin de générer le fichier `RH_Sport.csv`.

### 2. Génération des activités sportives

**Workflow :** `projet12_historique_strava`

Ce workflow génère des événements sportifs et les enregistre dans PostgreSQL.

### 3. Capture des nouveaux événements

**Workflow :** `projet12_trigger_postgresql_to_producer_strava_multi`

Ce workflow est déclenché automatiquement lors de l'ajout d'une nouvelle activité dans PostgreSQL. Les événements sont ensuite publiés dans Redpanda.

### 4. Consommation des événements

#### Publication Slack

**Workflow :** `projet12_consumers_to_slack`

Publie automatiquement les activités sportives dans le canal Slack dédié.

#### Alimentation du Data Warehouse

**Workflow :** `projet12_consumers_to_BI`

Consomme les événements Redpanda, enrichit les données et alimente la table de faits du Data Warehouse utilisée par Metabase.

### 5. Contrôle qualité

**Workflow :** `projet12_test`

Vérifie notamment la cohérence des volumes entre PostgreSQL et le Data Warehouse  ainsi que  la cohérence des données de mobilité. 


