FROM apache/spark:4.0.1-java21-r

USER root

RUN mkdir -p /opt/jdbc/jars/ && \
    curl -L -o /opt/jdbc/jars/postgresql-42.7.3.jar \
    https://jdbc.postgresql.org/download/postgresql-42.7.3.jar

USER spark

