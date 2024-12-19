from airflow import DAG
from airflow.decorators import task
from datetime import datetime
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.apps_settings')
django.setup()

default_args = {
    "owner": "thitiwok",
    "start_date": datetime(2024, 1, 1),
    "retries": 0,
}

with DAG(
    dag_id="django_model",
    default_args=default_args,
    schedule="0 * * * *",
    max_active_runs=1,
    catchup=False,
    tags=["app"],
) as dag:
    
    def taskflow_api():
        
        @task
        def test():
            print(os.environ.get('DJANGO_SETTINGS_MODULE'))
        
        test()
        
    taskflow_api()