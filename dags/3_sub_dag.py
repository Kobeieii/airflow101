from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta

default_args = {
    "owner": "thitiwok",
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    dag_id="sub_dag",
    default_args=default_args,
    schedule=None,
    max_active_runs=3,
    catchup=False,
    tags=["fruits"],
) as dag:
    import time

    def taskflow_api():

        @task
        def get_fruit(**kwargs):
            fruit = kwargs["dag_run"].conf["fruit"]
            return fruit

        @task
        def print_fruit(fruit):
            time.sleep(2)
            print(f"I love {fruit}s")

        fruit = get_fruit()
        print_fruit(fruit)

    taskflow_api()
