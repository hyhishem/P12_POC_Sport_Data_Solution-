# POC Sport Data Solution



## 1. Context et details


### Objectifs


### Technologies utilisées


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




docker build -t python-strava-pandas:latest -f Dockerfile  . 



