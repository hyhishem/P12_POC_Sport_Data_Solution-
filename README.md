# POC Sport Data Solution
 test
 

docker build -t pyspark-postgresjar -f dockerfile_image/Apach_postgresql/Dockerfile  .



docker build -t python-strava-pandas -f dockerfile_image/Python_pandas/Dockerfile  . 



while read -r line; do
    key="${line%%=*}"
    value="${line#*=}"

    echo "SECRET_${key}=$(printf '%s' "$value" | base64 -w 0)"
done < .env > .env_encoded



