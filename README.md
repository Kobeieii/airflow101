# Airflow with Docker Compose and Django

This project demonstrates how to set up Apache Airflow using Docker Compose, including a Django project for managing models and logic. Follow the steps below to get your Airflow environment up and running.

## Prerequisites

Ensure you have the following installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure
    .
    ├── dags                    # Directory where your DAGs are stored
    │   ├── example_dag.py      # Example DAG file
    ├── logs                    # Directory where your logs are stored
    ├── plugins                 # Directory where your custom plugins and Django project are stored
    │   ├── example_logic.py
    ├── docker-compose.yaml     # Docker Compose configuration file
    ├── Dockerfile              # Docker configuration file
    ├── requirements.txt        # Python dependencies
    └── README.md               # Project documentation


- `dags/`: Directory where your DAGs are stored.
- `logs/`: Directory where your logs are stored.
- `plugins/`: Directory where your custom plugins.
- `docker-compose.yaml`: Docker Compose configuration file.

## Usage

### Starting the Services

To start all services defined in the Docker Compose file, run:

```bash
docker-compose up -d
```
### Stopping the Services

To stop the services, run:
```bash
docker-compose down
```
### Accessing the Airflow Web UI
Once the services are up, you can access the Airflow web interface at http://localhost:8080. Log in with the credentials specified in the airflow-init service (username: `airflow`, password: `airflow`).

