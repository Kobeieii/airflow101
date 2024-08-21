FROM apache/airflow:2.7.3-python3.11

USER root
RUN curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
RUN curl https://packages.microsoft.com/config/debian/11/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools18
RUN sed -i 's/MinProtocol = TLSv1.2/MinProtocol = TLSv1/' /etc/ssl/openssl.cnf
RUN sed -i 's/CipherString = DEFAULT@SECLEVEL=2/CipherString = DEFAULT@SECLEVEL=1/' /etc/ssl/openssl.cnf

USER airflow

COPY requirements.txt /tmp/requirements.txt
ENV AIRFLOW_HOME=/opt/airflow
RUN pip install --no-cache-dir --user -r /tmp/requirements.txt