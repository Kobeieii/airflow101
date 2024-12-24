from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta

default_args = {
    "owner": "thitiwok",
    "start_date": datetime(2023, 1, 1),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="master_dag",
    default_args=default_args,
    schedule="0 0 * * *",
    max_active_runs=1,
    catchup=False,
    tags=["fruits"],
) as dag:

    def taskflow_api():

        @task
        def get_fruits():
            return ["apple", "banana", "cherry", "strawberry", "kiwi", "orange"]

        @task
        def trigger_dag(fruits):
            from airflow.operators.trigger_dagrun import TriggerDagRunOperator
            from airflow.operators.python import get_current_context

            context = get_current_context()
            for fruit in fruits:
                TriggerDagRunOperator(
                    task_id=f"trigger_dag_{fruit}",
                    trigger_dag_id="sub_dag",
                    conf={"fruit": fruit},
                ).execute(context)

        fruits = get_fruits()
        trigger_dag(fruits)

    taskflow_api()
