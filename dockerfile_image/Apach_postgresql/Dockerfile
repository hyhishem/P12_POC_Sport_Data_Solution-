FROM apache/spark:4.0.1-java21-r

USER root

RUN mkdir -p /opt/jdbc && \
    curl -L -o /opt/jdbc/postgresql-42.7.3.jar \
    https://jdbc.postgresql.org/download/postgresql-42.7.3.jar && \ 
    curl -L -o /opt/spark/jars/spark-sql-kafka-0-10_2.13-4.0.1.jar \ 
    https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.13/4.0.1/spark-sql-kafka-0-10_2.13-4.0.1.jar && \
    curl -L -o /opt/spark/jars/kafka-clients-3.4.0.jar \ 
    https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.4.0/kafka-clients-3.4.0.jar && \
    curl -L -o /opt/spark/jars/spark-token-provider-kafka-0-10_2.13-4.0.1.jar \
    https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.13/4.0.1/spark-token-provider-kafka-0-10_2.13-4.0.1.jar && \
    curl -L -o /opt/spark/jars/commons-pool2-2.11.1.jar \
    https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar

ENV SPARK_EXTRA_CLASSPATH=/opt/jdbc/postgresql-42.7.3.jar
ENV SPARK_CLASSPATH=/opt/jdbc/postgresql-42.7.3.jar


USER spark

